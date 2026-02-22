# Download or create this dataset
import pandas as pd
import numpy as np

# Simulate sensor data
np.random.seed(42)
n_records = 10000

sensor_data = {
    'train_id': np.random.choice(['BNSF-001', 'BNSF-002', 'BNSF-003', 'BNSF-004'], n_records),
    'timestamp': pd.date_range('2025-01-01', periods=n_records, freq='H'),
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

'''

---

### **PROBLEM STATEMENT:**
```
BNSF Railway - Sensor Data Quality System
==========================================

You are building a data quality system for BNSF's locomotive sensors.
The sensors occasionally malfunction, producing missing or anomalous readings.

Your task is to build a comprehensive data cleaning and anomaly detection pipeline.

INPUT:
- sensor_data.csv (10,000 records)
- Columns: train_id, timestamp, temperature, vibration, oil_pressure, 
           fuel_level, days_since_maintenance

PART 1 (20 minutes): Data Cleaning Function
--------------------------------------------
Write a function: clean_sensor_data(df)

Requirements:
1. Handle missing values:
   - For temperature & vibration: Use median of previous 5 readings for same train
   - If < 5 previous readings exist, use overall median
   - Drop rows where ALL sensor values are missing

2. Handle invalid values:
   - fuel_level must be between 0-100 (drop invalid rows)
   - temperature must be between -20 and 120 degrees
   - vibration must be between 0 and 15

3. Return:
   - cleaned DataFrame
   - Dictionary with statistics:
     {
       'total_rows': int,
       'rows_dropped': int,
       'values_imputed': int,
       'quality_score': float (0-100, based on % valid data)
     }

Example:
>>> result_df, stats = clean_sensor_data(df)
>>> print(stats)
{
  'total_rows': 10000,
  'rows_dropped': 127,
  'values_imputed': 483,
  'quality_score': 94.8
}


PART 2 (25 minutes): Anomaly Detection
---------------------------------------
Write a function: detect_anomalies(df)

Requirements:
1. Calculate rolling statistics for each train:
   - 7-day rolling average for temperature
   - 7-day rolling average for vibration
   - 7-day standard deviation for both

2. Flag anomalies where:
   - Current reading > (rolling_avg + 3 * rolling_std)
   - OR: Sudden spike (change > 50% from previous hour)
   
3. Calculate anomaly score per train:
   - score = (number of anomalies / total readings) * 100

4. Return:
   - DataFrame with new columns: 
     'temp_anomaly', 'vib_anomaly', 'anomaly_score'
   - List of train_ids that need immediate inspection (score > 5%)

Example:
>>> anomaly_df, flagged_trains = detect_anomalies(cleaned_df)
>>> print(flagged_trains)
['BNSF-002', 'BNSF-004']


PART 3 (25 minutes): Optimization Challenge
--------------------------------------------
The dataset will grow to 1 million records.

Optimize your functions for:
1. Time complexity: O(n) or O(n log n)
2. Memory efficiency: Process in chunks if needed
3. Handle edge cases:
   - Single train in dataset
   - All readings for a train are identical
   - First 7 days (no rolling window yet)

Write a function: process_large_dataset(file_path, chunk_size=10000)

That processes the data in chunks and returns aggregated results.

Requirements:
- Process CSV in chunks (don't load entire file)
- Return summary per train:
  {
    'train_id': str,
    'avg_temperature': float,
    'max_vibration': float,
    'total_anomalies': int,
    'quality_score': float
  }

Example:
>>> summary = process_large_dataset('large_sensor_data.csv')
>>> print(summary[0])
{
  'train_id': 'BNSF-001',
  'avg_temperature': 74.3,
  'max_vibration': 8.2,
  'total_anomalies': 12,
  'quality_score': 98.1
}


CONSTRAINTS:
- Time limit: 70 minutes total
- All functions must handle edge cases
- Code must be production-ready (error handling, logging)
- Optimize for large datasets (1M+ rows)

EVALUATION:
- Correctness: 50%
- Performance: 30%
- Code quality: 20%

'''