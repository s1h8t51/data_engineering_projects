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

import pandas as pd
import numpy as np

def prepare_data(df):
    df = df.copy()
    for col in ['maintenance_score', 'crew_experience_years']:
        df[col] = df[col].fillna(df[col].median())
        
    df['distance_per_ton'] = df['distance_miles'] / df['cargo_weight_tons']
    df['maintenance_per_age'] = df['maintenance_score'] / df['locomotive_age_years']
    df['is_heavy_cargo'] = (df['cargo_weight_tons'] > 6000).astype(int)
    df['is_old_locomotive'] = (df['locomotive_age_years'] > 15).astype(int)
    
    # FIX 2: Drop unique IDs and non-predictive strings before encoding
    # These cannot be converted to floats/numbers for the model
    df = df.drop(columns=['train_id', 'actual_duration_hours'], errors='ignore')
    
    # 3. Categorical Encoding (Handles route and weather)
    df = pd.get_dummies(df, columns=['route', 'weather_condition'], drop_first=True)
    
    y = df['delayed']
    X = df.drop(columns=['delayed'])
    
    return X, y, X.columns.tolist()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def train_delay_predictor(X, y):
    # 1. Stratified Split (Crucial for class imbalance)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    
    # 2. Define Pipelines
    models = {
        'LogisticReg': LogisticRegression(max_iter=1000),
        'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42)
    }
    
    comparison_list = []
    trained_pipes = {}
    
    for name, model in models.items():
        pipe = Pipeline([
            ('scaler', RobustScaler()),
            ('clf', model)
        ])
        
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)
        
        # 3. Calculate Metrics
        metrics = {
            'model_name': name,
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred),
            'accuracy': accuracy_score(y_test, y_pred)
        }
        comparison_list.append(metrics)
        trained_pipes[name] = pipe

    # 4. Results Processing
    comparison_df = pd.DataFrame(comparison_list)
    best_model_name = comparison_df.sort_values(by='f1_score', ascending=False).iloc[0]['model_name']
    best_pipe = trained_pipes[best_model_name]
    
    # Extract Feature Importances (From Random Forest specifically)
    rf_model = trained_pipes['RandomForest'].named_steps['clf']
    importances = pd.DataFrame({
        'feature': X.columns,
        'importance': rf_model.feature_importances_
    }).sort_values(by='importance', ascending=False)

    return best_pipe, comparison_df, importances

def predict_delays_batch(new_data, model_pipeline):
    if new_data.empty:
        raise ValueError("Input data is empty")

    # 1. & 2. Preprocessing is handled by the model_pipeline itself!
    # (Assuming new_data has passed through the same prepare_data function)
    
    # 3. Predictions with Confidence Scores
    # [:, 1] gets the probability of the "Delayed" class (1)
    probabilities = model_pipeline.predict_proba(new_data)[:, 1]
    predictions = model_pipeline.predict(new_data)
    
    # 4. Create Predictions DataFrame
    results_df = pd.DataFrame({
        'train_id': new_data.get('train_id', range(len(new_data))),
        'predicted_delay': predictions,
        'confidence': probabilities
    })
    
    # Flag high-risk trains (confidence > 70%)
    results_df['risk_level'] = np.where(results_df['confidence'] > 0.7, 'High Risk', 'Standard')
    
    # 5. Summary Statistics
    summary = {
        'total_trains': int(len(results_df)),
        'predicted_delays': int(results_df['predicted_delay'].sum()),
        'high_risk_count': int((results_df['risk_level'] == 'High Risk').sum()),
        'avg_confidence': float(results_df['confidence'].mean())
    }
    
    return results_df, summary

X, y, feature_names = prepare_data(df)

# 3. Train and Compare Models
best_model, comparison_df, top_features = train_delay_predictor(X, y)

# --- PRINT OUTPUTS ---
print("\n--- MODEL COMPARISON ---")
print(comparison_df)

print("\n--- TOP 10 FEATURES ---")
print(top_features)

# 4. Production Test: Predict on 5 new trains
new_data_sample = X.head(5) 
predictions, summary = predict_delays_batch(new_data_sample, best_model)

print("\n--- BATCH PREDICTION SUMMARY ---")
print(summary)

print("\n--- DETAILED PREDICTIONS ---")
print(predictions)