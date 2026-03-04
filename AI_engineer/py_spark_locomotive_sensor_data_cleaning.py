from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

def clean_sensor_data_pyspark(df):
    initial_row_count = df.count()
    sensor_cols = ["temperature", "vibration", "oil_pressure", "fuel_level"]
    window_spec = Window.partitionBy("train_id").orderBy("timestamp").rowsBetween(-5, -1)
    
    # 2. IMPUTATION (Rolling Median & Overall Median)
    # Note: Spark doesn't have a native 'median' in Window, so we use percentile_approx
    df_imputed = df
    imputed_count_total = 0
    
    for col_name in ["temperature", "vibration"]:
        overall_median = df.select(F.percentile_approx(col_name, 0.5)).collect()[0][0]
        rolling_median = F.percentile_approx(col_name, 0.5).over(window_spec)
        df_imputed = df_imputed.withColumn(
            col_name, 
            F.coalesce(F.col(col_name), rolling_median, F.lit(overall_median))
        )
    df_clean = df_imputed.dropna(how='all', subset=sensor_cols)
    # Apply Business Rules (Range Checks)
    df_clean = df_clean.filter(
        (F.col("fuel_level").between(0, 100)) &
        (F.col("temperature").between(-20, 120)) &
        (F.col("vibration").between(0, 15))
    )

    # 4. STATS CALCULATION
    final_row_count = df_clean.count()
    rows_dropped = initial_row_count - final_row_count
    
    # Quality Score Calculation
    total_columns = len(df_clean.columns)
    total_cells = final_row_count * total_columns
    
    # Count nulls across all columns efficiently
    null_counts = df_clean.select([F.sum(F.col(c).isNull().cast("int")).alias(c) for c in df_clean.columns])
    total_nulls = sum(null_counts.collect()[0])
    
    quality_score = ((total_cells - total_nulls) / total_cells) * 100

    stats = {
        'original_df_rows': initial_row_count,
        'total_rows': final_row_count,
        'rows_dropped': rows_dropped,
        'quality_score': round(float(quality_score), 2)
    }

    return df_clean, stats
from pyspark.sql import functions as F
from pyspark.sql.window import Window

def anomaly_detection(df):
    # 1. Windows: One for 7-day rolling, one for 1-hour lag
    rolling_window = Window.partitionBy("train_id").orderBy("timestamp").rowsBetween(-6, 0)
    lag_window = Window.partitionBy("train_id").orderBy("timestamp")

    cols_to_process = ["temperature", "vibration"]

    # 2. Rolling Average & Std Dev
    for col in cols_to_process:
        df = df.withColumn(f"{col}_roll_avg", F.avg(col).over(rolling_window)) \
               .withColumn(f"{col}_roll_std", F.stddev(col).over(rolling_window))

    # 3. Sudden Spike Logic (>50% change from previous reading)
    # pct_change formula: (current - previous) / previous
    for col in cols_to_process:
        prev_val = F.lag(F.col(col), 1).over(lag_window)
        spike_col = f"{col}_spike"
        df = df.withColumn(
            spike_col, 
            F.when(prev_val.isNotNull(), (F.col(col) - prev_val) / prev_val > 0.50)
             .otherwise(False).cast("int")
        )

    # 4. Statistical Anomaly Logic (Z-Score > 3)
    df = df.withColumn("temp_stat_anomaly", 
                       (F.col("temperature") > (F.col("temperature_roll_avg") + (3 * F.col("temperature_roll_std")))).cast("int")) \
           .withColumn("vib_stat_anomaly", 
                       (F.col("vibration") > (F.col("vibration_roll_avg") + (3 * F.col("vibration_roll_std")))).cast("int"))

    # 5. Combining Flags (Logical OR)
    df = df.withColumn("temp_anomaly", (F.col("temp_stat_anomaly") | F.col("temp_spike")).cast("int")) \
           .withColumn("vib_anomaly", (F.col("vib_stat_anomaly") | F.col("vib_spike")).cast("int")) \
           .withColumn("is_any_anomaly", (F.col("temp_anomaly") | F.col("vib_anomaly")).cast("int"))

    # 6. Calculating Anomaly Score (Grouped by train_id)
    # We use a Window instead of map() to keep it in the same DataFrame
    score_window = Window.partitionBy("train_id")
    df = df.withColumn("anomaly_score", 
                       (F.sum("is_any_anomaly").over(score_window) / F.count("is_any_anomaly").over(score_window)) * 100)

    # 7. Create Inspection List (Trains with > 5% anomaly rate)
    inspection_list = df.filter(F.col("anomaly_score") > 5) \
                        .select("train_id").distinct() \
                        .rdd.flatMap(lambda x: x).collect()

    return df, inspection_list

def process_large_dataset(file_path, chunk_size=10000):
    train_status ={}
    for chunk in spark.read.format("csv").load(file_path):
        cleaned_chunk, _ = clean_sensor_data_pyspark(chunk)
        flagged_chunk, _ = anomaly_detection(cleaned_chunk)
        for train_id, data in flagged_chunk.groupBy('train_id'):
            if train_id not in train_stats:
                train_stats[train_id] = { 
                'temp_sum': 0, 'temp_count': 0,
                'max_vib': 0, 'total_anamolies': 0,
                'total_rows': 0, 'valid_cells': 0
                }
            
            ts = train_stats[train_id]
            ts['temp_sum']    += data['temperature'].sum()
            ts['temp_count']  += data['temperature'].count()
            ts['max_vib']      = max(ts['max_vib'], data['vibration'].max())
            ts['total_anamolies'] += data['is_any_anomaly'].sum() # FIXED: Check your spelling of 'anamoly'
            ts['total_rows']   += len(data)
            ts['valid_cells']  += data[['temperature', 'vibration', 'fuel_level']].notnull().sum().sum()
    final_summary = []
    for t_id, stats in train_stats.items(): # FIXED: Use t_id from items()
        summary = {
            'train_id': t_id,
            'avg_temperature': stats['temp_sum'] / stats['temp_count'] if stats['temp_count'] > 0 else 0,
            'max_vibration': stats['max_vib'],
            'total_anamolies': int(stats['total_anamolies']),
            'quality_score': (stats['valid_cells'] / (stats['total_rows'] * 3)) * 100 
        }
        final_summary.append(summary) # FIXED: Actually add the summary to the list
        
    return final_summary




# --- EXECUTION IN DATABRICKS ---
spark = SparkSession.builder.appName("LocomotiveCleaning").getOrCreate()
# Load your CSV as a Spark DataFrame
raw_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/path/to/sensors.csv")

cleaned_df, cleaning_stats = clean_sensor_data_pyspark(raw_df)
print(cleaning_stats)

# Save as Delta for Time Travel and Performance
cleaned_df.write.format("delta").mode("overwrite").saveAsTable("locomotive_master_clean")