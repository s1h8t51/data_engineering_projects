import pandas as pd
import numpy as np

# Simulate train delay data
np.random.seed(123)
n_trains = 5000

delay_data = {
    'train_id': [f'TRAIN-{i:04d}' for i in range(n_trains)],
    'route': np.random.choice(['Chicago-Seattle', 'Denver-LA', 'Texas-Portland'], n_trains),
    'distance_miles': np.random.randint(500, 2000, n_trains),
    'weather_condition': np.random.choice(['Clear', 'Rain', 'Snow', 'Fog'], n_trains),
    'cargo_weight_tons': np.random.randint(1000, 8000, n_trains),
    'scheduled_duration_hours': np.random.randint(24, 96, n_trains),
    'actual_duration_hours': None,  # Will calculate
    'crew_experience_years': np.random.randint(1, 25, n_trains),
    'locomotive_age_years': np.random.randint(1, 30, n_trains),
    'maintenance_score': np.random.uniform(60, 100, n_trains),
}

df = pd.DataFrame(delay_data)

# Calculate actual duration (with delays)
base_delay = 0
weather_delay = df['weather_condition'].map({'Clear': 0, 'Rain': 2, 'Snow': 5, 'Fog': 3})
weight_delay = (df['cargo_weight_tons'] - 4000) / 500  # heavier = slower
age_delay = df['locomotive_age_years'] / 10

df['actual_duration_hours'] = (
    df['scheduled_duration_hours'] + 
    weather_delay + 
    weight_delay + 
    age_delay + 
    np.random.normal(0, 3, n_trains)
)

# Create binary target: delayed (>2 hours late)
df['delayed'] = (df['actual_duration_hours'] - df['scheduled_duration_hours'] > 2).astype(int)

# Introduce missing values
df.loc[df.sample(frac=0.05).index, 'maintenance_score'] = np.nan
df.loc[df.sample(frac=0.03).index, 'crew_experience_years'] = np.nan

df.to_csv('train_delays.csv', index=False)

'''

---

### **PROBLEM STATEMENT:**
```
BNSF Railway - Delay Prediction System
=======================================

Build a machine learning pipeline to predict train delays.

INPUT: train_delays.csv (5,000 records)

PART 1 (15 minutes): Data Preparation
--------------------------------------
Write a function: prepare_data(df)

Requirements:
1. Handle missing values:
   - maintenance_score: fill with median
   - crew_experience_years: fill with median
   
2. Encode categorical variables:
   - route: one-hot encoding
   - weather_condition: one-hot encoding
   
3. Create new features:
   - distance_per_ton = distance / cargo_weight
   - maintenance_per_age = maintenance_score / locomotive_age
   - is_heavy_cargo = 1 if cargo_weight > 6000 else 0
   - is_old_locomotive = 1 if age > 15 else 0

4. Return:
   - X (features), y (target: delayed)
   - Feature names list


PART 2 (30 minutes): Model Training & Evaluation
-------------------------------------------------
Write a function: train_delay_predictor(X, y)

Requirements:
1. Split data: 80% train, 20% test (stratified)

2. Train THREE models:
   - Logistic Regression
   - Random Forest (100 trees)
   - XGBoost (if you know it, otherwise skip)

3. For each model, calculate:
   - Precision
   - Recall
   - F1 Score
   - Accuracy

4. Return:
   - Best model (highest F1 score)
   - Comparison DataFrame with all metrics
   - Feature importances (top 10)

Example output:
>>> model, comparison, importances = train_delay_predictor(X, y)
>>> print(comparison)
   model_name  precision  recall  f1_score  accuracy
0  LogisticReg     0.72    0.68      0.70      0.73
1  RandomForest    0.81    0.78      0.79      0.82

>>> print(importances.head())
           feature  importance
0  distance_miles      0.234
1  cargo_weight        0.187
2  weather_Snow        0.156


PART 3 (25 minutes): Production Deployment
-------------------------------------------
Write a function: predict_delays_batch(new_data, model)

Requirements:
1. Accept new train data (same format as training)
2. Apply same preprocessing pipeline
3. Make predictions with confidence scores
4. Flag high-risk trains (confidence > 70% for delay)

5. Return:
   - Predictions DataFrame with:
     'train_id', 'predicted_delay', 'confidence', 'risk_level'
   - Summary statistics:
     {
       'total_trains': int,
       'predicted_delays': int,
       'high_risk_count': int,
       'avg_confidence': float
     }

Example:
>>> predictions, summary = predict_delays_batch(new_df, model)
>>> print(summary)
{
  'total_trains': 100,
  'predicted_delays': 23,
  'high_risk_count': 8,
  'avg_confidence': 0.76
}


CONSTRAINTS:
- Must use sklearn
- Handle edge cases (empty data, single class, etc.)
- Code must be efficient (< 5 seconds for 5000 records)
- Production-ready error handling

EVALUATION:
- Model performance: 40%
- Code correctness: 35%
- Feature engineering: 25%

'''