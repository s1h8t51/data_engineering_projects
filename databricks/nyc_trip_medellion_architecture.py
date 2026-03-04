from pyspark.sql import functions as F

from databricks.connect import DatabricksSession
spark = DatabricksSession.builder.getOrCreate()
# 1️⃣ Bronze ingestion
df_bronze = spark.table("samples.nyctaxi.trips") \
    .withColumn("_ingested_at", F.current_timestamp()) \
    .withColumn("_source_table", F.lit("nyctaxi.trips")) \
    .withColumn("_batch_id", F.lit("batch_001"))

# Quarantine bad rows
df_quarantine = df_bronze.filter(
    (F.col("trip_distance") <= 0) |
    (F.col("fare_amount") < 0) |
    F.col("pickup_zip").isNull() |
    F.col("dropoff_zip").isNull()
)
df_quarantine.write.format("delta").mode("append").saveAsTable("workspace.bronze.nyctaxi_quarantine")

# 2️⃣ Silver transformation
df_silver = df_bronze.dropDuplicates(["tpep_pickup_datetime","tpep_dropoff_datetime","trip_distance","pickup_zip"]) \
    .filter(
        (F.col("trip_distance") > 0) &
        (F.col("fare_amount") >= 0) &
        F.col("pickup_zip").isNotNull() &
        F.col("dropoff_zip").isNotNull()
    ) \
    .withColumn("trip_duration_minutes", 
                (F.col("tpep_dropoff_datetime").cast("long") - F.col("tpep_pickup_datetime").cast("long"))/60) \
    .withColumn("fare_per_mile", 
                (F.col("fare_amount") / F.col("trip_distance")).cast("decimal(10,2)")) \
    .withColumn("fare_amount", F.col("fare_amount").cast("decimal(10,2)")) \
    .withColumn("trip_distance", F.col("trip_distance").cast("decimal(10,2)"))

df_silver.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("pickup_zip") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver.nyctaxi_trips")

# 3️⃣ Delta optimizations
spark.sql("OPTIMIZE silver.nyctaxi_trips ZORDER BY (tpep_pickup_datetime)")
spark.sql("VACUUM silver.nyctaxi_trips RETAIN 168 HOURS")

# 4️⃣ Gold aggregation
df_gold = df_silver.groupBy("pickup_zip","dropoff_zip") \
    .agg(
        F.avg("trip_distance").alias("avg_trip_distance"),
        F.avg("fare_amount").alias("avg_fare_amount"),
        F.avg("fare_per_mile").alias("avg_fare_per_mile")
    )

df_gold.write.format("delta").mode("overwrite").saveAsTable("gold.nyctaxi_summary")

