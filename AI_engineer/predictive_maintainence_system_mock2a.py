import pandas as pd
import numpy as np

np.random.seed(456)
n_locomotives = 8000

maintenance_data = {
    'locomotive_id': [f'LOC-{i:04d}' for i in range(n_locomotives)],
    'engine_hours': np.random.randint(1000, 50000, n_locomotives),
    'avg_speed_mph': np.random.uniform(40, 70, n_locomotives),
    'total_miles': np.random.randint(50000, 500000, n_locomotives),
    'oil_change_interval': np.random.randint(100, 300, n_locomotives),
    'brake_thickness_mm': np.random.uniform(5, 25, n_locomotives),
    'wheel_wear_score': np.random.uniform(0, 100, n_locomotives),
    'temperature_avg': np.random.normal(75, 10, n_locomotives),
    'vibration_avg': np.random.normal(5, 2, n_locomotives),
    'fuel_efficiency_mpg': np.random.uniform(0.15, 0.35, n_locomotives),
    'last_maintenance_days': np.random.randint(1, 180, n_locomotives),
}

df = pd.DataFrame(maintenance_data)

# Create failure probability based on features
failure_prob = (
    (df['engine_hours'] / 50000) * 0.3 +
    (df['last_maintenance_days'] / 180) * 0.3 +
    ((25 - df['brake_thickness_mm']) / 25) * 0.2 +
    ((100 - df['wheel_wear_score']) / 100) * 0.2
)

# Add noise
failure_prob += np.random.normal(0, 0.1, n_locomotives)
failure_prob = np.clip(failure_prob, 0, 1)

# Create binary target
df['needs_maintenance'] = (failure_prob > 0.6).astype(int)

# Add maintenance cost (higher for older/more worn equipment)
df['estimated_cost'] = (
    500 + 
    (df['engine_hours'] / 1000) * 10 +
    (180 - df['last_maintenance_days']) * 2 +
    np.random.normal(0, 100, n_locomotives)
)

df.to_csv('locomotive_maintenance.csv', index=False)

'''

---

### **PROBLEM STATEMENT:**
```
BNSF Railway - Predictive Maintenance AI System
================================================

Build an AI system to predict which locomotives need immediate maintenance.

INPUT: locomotive_maintenance.csv (8,000 records)

PART 1 (20 minutes): Feature Engineering
-----------------------------------------
Write a function: engineer_maintenance_features(df)

Requirements:
1. Create composite features:
   - usage_intensity = total_miles / engine_hours
   - maintenance_risk_score = (wheel_wear / 100) * (brake_thickness / 25)
   - efficiency_degradation = 1 - (fuel_efficiency / 0.35)
   - critical_parts_score = MIN(brake_thickness, wheel_wear_score) / 100
   
2. Create time-based features:
   - maintenance_overdue = 1 if last_maintenance_days > 90 else 0
   - high_mileage = 1 if total_miles > 300000 else 0
   - engine_critical = 1 if engine_hours > 40000 else 0

3. Scale numerical features:
   - Standardize: engine_hours, total_miles, temperature_avg
   - Normalize to 0-1: all _score features

4. Return:
   - Enhanced DataFrame with new features
   - List of feature names to use for modeling

Test case:
>>> enhanced_df, feature_list = engineer_maintenance_features(df)
>>> print(len(feature_list))  # Should be ~15-20 features
>>> print(enhanced_df['maintenance_risk_score'].describe())


PART 2 (30 minutes): Build Maintenance Predictor
-------------------------------------------------
Write a function: build_maintenance_model(X, y)

Requirements:
1. Handle class imbalance:
   - Check class distribution
   - If imbalanced, use SMOTE or class_weight='balanced'

2. Train and compare models:
   a) Logistic Regression (baseline)
   b) Random Forest (n_estimators=200, max_depth=10)
   c) Gradient Boosting (n_estimators=100)

3. Use 5-fold cross-validation for each model

4. For each model, calculate:
   - Precision (critical: avoid false alarms)
   - Recall (critical: catch all failures)
   - F1 Score
   - ROC-AUC
   - Confusion matrix

5. Return:
   - Best model (optimize for F1 score)
   - Cross-validation results DataFrame
   - Feature importances (top 15)
   - Recommended threshold (balance precision/recall)

Example:
>>> model, cv_results, features, threshold = build_maintenance_model(X, y)
>>> print(cv_results)
      model  mean_f1  std_f1  mean_precision  mean_recall
0  LogReg     0.76   0.03          0.74         0.78
1  RF         0.84   0.02          0.83         0.85
2  GBM        0.86   0.02          0.87         0.85

>>> print(f"Best threshold: {threshold}")  # e.g., 0.42


PART 3 (20 minutes): Cost-Benefit Analysis
-------------------------------------------
Write a function: optimize_maintenance_schedule(df, model, cost_params)

Given:
- cost_params = {
    'preventive_maintenance': 500,  # scheduled maintenance cost
    'failure_repair': 5000,         # emergency repair if failure
    'false_alarm': 200              # cost of unnecessary inspection
  }

Requirements:
1. For each locomotive, predict:
   - Failure probability
   - Recommended action: maintain_now, monitor, or ok

2. Calculate expected cost:
   - If predict "maintain" when actually needs it: $500 (save $4500)
   - If predict "maintain" when doesn't need it: $500 + $200 = $700 (false alarm)
   - If miss failure prediction: $5000 (emergency repair)
   - If correctly predict "ok": $0

3. Compare strategies:
   - Current strategy: maintain all locomotives > 90 days
   - AI strategy: use model predictions
   - Calculate total cost savings

4. Return:
   - Maintenance schedule DataFrame:
     ['locomotive_id', 'probability', 'action', 'estimated_cost', 'priority']
   - Cost comparison:
     {
       'current_strategy_cost': float,
       'ai_strategy_cost': float,
       'savings': float,
       'savings_percentage': float
     }

Example:
>>> schedule, cost_analysis = optimize_maintenance_schedule(df, model, cost_params)
>>> print(cost_analysis)
{
  'current_strategy_cost': 2400000,
  'ai_strategy_cost': 1650000,
  'savings': 750000,
  'savings_percentage': 31.25
}


CONSTRAINTS:
- Handle imbalanced data properly
- Optimize for business value (cost savings)
- Model must run in < 10 seconds
- Production-ready code with error handling

EVALUATION:
- Model quality: 40%
- Feature engineering: 30%
- Business logic: 30%

'''