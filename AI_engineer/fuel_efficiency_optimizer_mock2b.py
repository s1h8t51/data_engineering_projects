import pandas as pd
import numpy as np

np.random.seed(789)
n_trips = 12000

fuel_data = {
    'trip_id': [f'TRIP-{i:05d}' for i in range(n_trips)],
    'route': np.random.choice(['Route-A', 'Route-B', 'Route-C', 'Route-D'], n_trips),
    'distance_miles': np.random.randint(200, 1500, n_trips),
    'cargo_weight_tons': np.random.randint(2000, 8000, n_trips),
    'avg_speed_mph': np.random.uniform(35, 65, n_trips),
    'elevation_gain_ft': np.random.randint(0, 5000, n_trips),
    'num_stops': np.random.randint(0, 15, n_trips),
    'weather': np.random.choice(['Clear', 'Rain', 'Wind', 'Snow'], n_trips),
    'temperature_f': np.random.randint(20, 95, n_trips),
    'locomotive_type': np.random.choice(['Diesel-A', 'Diesel-B', 'Hybrid'], n_trips),
}

df = pd.DataFrame(fuel_data)

# Calculate fuel consumption (gallons)
base_fuel = df['distance_miles'] * 0.25  # base: 0.25 gal/mile
weight_impact = (df['cargo_weight_tons'] / 1000) * 20
elevation_impact = (df['elevation_gain_ft'] / 1000) * 15
speed_impact = ((df['avg_speed_mph'] - 50) ** 2) * 0.5
weather_impact = df['weather'].map({'Clear': 0, 'Rain': 10, 'Wind': 15, 'Snow': 25})
stops_impact = df['num_stops'] * 5

df['fuel_gallons'] = (
    base_fuel + weight_impact + elevation_impact + 
    speed_impact + weather_impact + stops_impact +
    np.random.normal(0, 20, n_trips)
)
df['fuel_gallons'] = np.maximum(df['fuel_gallons'], 50)  # minimum 50 gallons

# Calculate efficiency
df['mpg'] = df['distance_miles'] / df['fuel_gallons']

df.to_csv('fuel_consumption.csv', index=False)


'''

---

### **PROBLEM STATEMENT:**
```
BNSF Railway - Fuel Efficiency ML System
=========================================

Build a system to predict and optimize fuel consumption.

INPUT: fuel_consumption.csv (12,000 trips)

PART 1 (15 minutes): Exploratory Analysis & Features
-----------------------------------------------------
Write a function: analyze_fuel_patterns(df)

Requirements:
1. Calculate statistics per route:
   - Average MPG
   - Average fuel consumption
   - Most efficient speed range
   - Impact of cargo weight on MPG

2. Identify efficiency patterns:
   - Best performing locomotive type
   - Optimal number of stops
   - Weather impact on fuel

3. Create efficiency features:
   - weight_per_mile = cargo_weight / distance
   - elevation_per_mile = elevation_gain / distance
   - speed_efficiency_score = 1 / (abs(avg_speed - 50) + 1)
   - efficiency_rating = 'High' if mpg > 4 else 'Medium' if mpg > 3 else 'Low'

4. Return:
   - Statistics dictionary
   - Enhanced DataFrame with new features

Example:
>>> stats, enhanced_df = analyze_fuel_patterns(df)
>>> print(stats['route_efficiency'])
   route  avg_mpg  best_speed_range  best_locomotive
0  Route-A   3.8      45-55          Hybrid
1  Route-B   3.4      40-50          Diesel-B


PART 2 (35 minutes): Fuel Consumption Predictor
------------------------------------------------
Write a function: train_fuel_model(df)

Requirements:
1. Prepare data:
   - Target: fuel_gallons (regression problem)
   - Features: all except trip_id, mpg, efficiency_rating
   - Encode categorical variables
   - Split: 70% train, 15% validation, 15% test

2. Train THREE regression models:
   - Linear Regression (baseline)
   - Random Forest Regressor (200 trees)
   - Gradient Boosting Regressor (100 trees)

3. For each model, calculate:
   - MAE (Mean Absolute Error)
   - RMSE (Root Mean Squared Error)
   - R² score
   - MAPE (Mean Absolute Percentage Error)

4. Feature analysis:
   - Feature importances
   - Correlation with target
   - Identify top 5 fuel-saving opportunities

5. Return:
   - Best model
   - Performance comparison DataFrame
   - Feature importances
   - Validation predictions vs actuals

Example:
>>> model, performance, features, predictions = train_fuel_model(df)
>>> print(performance)
      model   MAE   RMSE   R2   MAPE
0  LinearReg  28.4  35.2  0.76  8.2%
1  RF         18.2  23.1  0.89  5.3%
2  GBM        15.7  20.4  0.92  4.7%


PART 3 (20 minutes): Route Optimization
----------------------------------------
Write a function: optimize_route_fuel(route_data, model)

Given a new trip:
{
  'route': 'Route-B',
  'distance': 800 miles,
  'cargo_weight': 5000 tons,
  'elevation_gain': 2000 ft
}

Requirements:
1. Predict fuel consumption under different conditions:
   - Various speeds (35-65 mph)
   - Different locomotive types
   - Different stop strategies (0-10 stops)

2. Find optimal configuration:
   - Speed that minimizes fuel
   - Best locomotive type
   - Recommended number of stops
   - Estimated fuel savings vs. standard operation

3. Consider constraints:
   - Speed must be 40-60 mph (safety/schedule)
   - Must use available locomotive types
   - Stops depend on route requirements

4. Return:
   - Optimization results:
     {
       'optimal_speed': float,
       'optimal_locomotive': str,
       'optimal_stops': int,
       'predicted_fuel': float,
       'standard_fuel': float,
       'savings_gallons': float,
       'savings_dollars': float (at $3.50/gallon)
     }
   - Sensitivity analysis (fuel vs speed chart data)

Example:
>>> optimization = optimize_route_fuel(trip_params, model)
>>> print(optimization)
{
  'optimal_speed': 48.5,
  'optimal_locomotive': 'Hybrid',
  'optimal_stops': 3,
  'predicted_fuel': 215.3,
  'standard_fuel': 267.8,
  'savings_gallons': 52.5,
  'savings_dollars': 183.75
}


CONSTRAINTS:
- Must handle regression (not classification)
- Optimize for business value (fuel cost)
- Consider operational constraints
- Code must be efficient

EVALUATION:
- Prediction accuracy: 40%
- Optimization logic: 35%
- Feature engineering: 25%
'''