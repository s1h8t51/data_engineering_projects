# Download or create this dataset
import pandas as pd
import numpy as np

# Simulate sensor data
np.random.seed(42)
n_records = 10000

sensor_data = {
    'train_id': np.random.choice(['BNSF-001', 'BNSF-002', 'BNSF-003', 'BNSF-004'], n_records),
    'timestamp': pd.date_range('2025-01-01', periods=n_records, freq='h'),
    'temperature': np.random.normal(75, 15, n_records),
    'vibration': np.random.normal(5, 2, n_records),
    'oil_pressure': np.random.normal(40, 8, n_records),
    'fuel_level': np.random.uniform(10, 100, n_records),
    'days_since_maintenance': np.random.randint(0, 90, n_records)
}

df = pd.DataFrame(sensor_data)

# Introduce problems:
# 1. Random missing values (5%)
df.loc[df.sample(frac=0.05).index, 'temperature'] = np.nan

df.loc[df.sample(frac=0.05).index, 'vibration'] = np.nan

# 2. Outliers (2%)
df.loc[df.sample(frac=0.02).index, 'temperature'] = np.random.uniform(150, 200, int(n_records*0.02))
df.loc[df.sample(frac=0.02).index, 'vibration'] = np.random.uniform(20, 30, int(n_records*0.02))

# 3. Invalid values
df.loc[df.sample(frac=0.01).index, 'fuel_level'] = -1  # Invalid negative fuel

# Save to CSV
df.to_csv('sensor_data.csv', index=False)


def clean_sensor_data(df):
   initial_row_count = len(df)
   df_clean =df.copy()
   sensor_cols = ["temperature","vibration","oil_pressure","fuel_level"] #important cols
   imputed_count = 0
   for col in ["temperature","vibration"]:
      is_null = df_clean[col].isnull()
      imputed_count += is_null.sum()
      rolling_median = df_clean.groupby("train_id")[col].transform(lambda x :x.shift(1).rolling(window=5,min_periods = 1).median())
      overall_meadian = df_clean[col].median()
      df_clean[col] =df_clean[col].fillna(rolling_median).fillna(overall_meadian)

   df_clean = df_clean.dropna(how ='all',subset=sensor_cols) #drop all rows where sensor values missing 
   #fuel_levl 0-100
   df_clean = df_clean[(df_clean["fuel_level"] >= 0) & (df_clean["fuel_level"] <= 100)]
   # temperature -20 to 120
   df_clean = df_clean[(df_clean["temperature"] >= -20) & (df_clean["temperature"] <= 120)]
   # vibration 0 to 15
   df_clean = df_clean[(df_clean.vibration >= 0) & (df_clean.vibration <= 15)]
   df_clean = df_clean.sort_values(["train_id","timestamp"])
   

   final_row_count = len(df_clean)
   rows_dropped = initial_row_count  - final_row_count
   # quality score claculation    
   total_cells = final_row_count * (len(df_clean.columns))
   null_cells = df_clean.isnull().sum().sum()
   quality_score = ((total_cells - null_cells) / total_cells )*100
   stats ={
      'original_df_rows':initial_row_count ,
      'total_rows': final_row_count,
      'rows_dropped': rows_dropped,
      'values_imputed': int(imputed_count),
      'quality_score': round(float(quality_score),2)
      }
   return df_clean,stats
    


def anamoly_detection(df):
   #7 day rolling average of temparature and vibration 
   # 7 day standard deviation for both 
   df = df.sort_values(["train_id","timestamp"])
   for col in ["temperature","vibration"]:
      group = df.groupby("train_id")[col]
      df[f'{col}_roll_avg'] = group.transform(lambda x :x.shift(1).rolling(window=7,min_periods = 1).mean())
      df[f'{col}_roll_std'] =group.transform(lambda x :x.shift(1).rolling(window=7,min_periods = 1).std())
   #flag anamolies
   #condition Current reading > (rolling_avg + 3 * rolling_std)
   df["temp_anomaly"] = df["temperature"] > (df["temperature_roll_avg"] + (3* df["temperature_roll_std"]))
   df["vib_anomaly"] = df["vibration"] > (df["vibration_roll_avg"] + (3* df["vibration_roll_std"]))

   #condition :change  sudden spike >50% change from previous hpur
   df['temp_spike'] = df.groupby("train_id")["temperature"] .transform(lambda x :x.pct_change().fillna(0) > 0.50)
   df['vib_spike'] = df.groupby("train_id")["vibration"] .transform(lambda x :x.pct_change().fillna(0) > 0.50)

   #combining_flags 
   df["temp_anomaly"] = df.temp_anomaly | df.temp_spike
   df["vib_anomaly"] = df.vib_anomaly| df.vib_spike

   #calculating anamoly score 
   df["is_any_anomaly"] = df['temp_anomaly'] | df['vib_anomaly']
   anamoly_counts = df.groupby("train_id")["is_any_anomaly"].sum()    
   total_readings = df.groupby("train_id")["is_any_anomaly"].count()
   scores = (anamoly_counts / total_readings) *100

   #mapping scores back to dataframe 
   df['anomaly_score'] = df.train_id.map(scores)
   inspection_list = scores[scores >5].index.tolist()
   cols_to_keep = list(df.columns[:df.columns.get_loc('temp_anomaly')+1])+ ['vib_anomaly','anomaly_score']

   return df, inspection_list

def process_large_datasets(file_path, chunk_size=10000):
   train_stats = {} # Initialize empty dictionary once
   
   for chunk in pd.read_csv(file_path, chunksize=chunk_size):
      # FIXED: Pass cleaned data to anomaly detection
      cleaned_chunk, _ = clean_sensor_data(chunk)
      flagged_chunk, _ = anamoly_detection(cleaned_chunk) 

      for train_id, data in flagged_chunk.groupby('train_id'):
         # FIXED: Only initialize if this SPECIFIC train_id is new
         if train_id not in train_stats:
            train_stats[train_id] = { # FIXED: Key into the specific train
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

   # FIXED: Move final_summary OUTSIDE the chunk loop
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





# Capture the clean data first
df_cleaned_final, stats = clean_sensor_data(df)

# Pass the CLEANED data into the anomaly detector
df_anomalies, high_risk_trains = anamoly_detection(df_cleaned_final)
final_summary = process_large_datasets("sensor_data.csv")


print(stats)
print(high_risk_trains)
print(final_summary)



      

