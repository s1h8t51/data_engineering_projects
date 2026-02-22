# 🎯 BNSF CODILITY ASSESSMENT - WHAT TO EXPECT

## 📊 ASSESSMENT DETAILS

**Duration:** 70 minutes
**Tasks:** 1 task (unusual - typically 2-3, but BNSF specified "1 task")
**Platform:** Codility
**Language:** Python
**Test date:** Feb 25 (Tuesday) - 3 days away

---

## 🔍 WHAT "1 TASK" LIKELY MEANS

**Two possible scenarios:**

### **SCENARIO A: One Complex Multi-Part Problem (70% probability)** ⭐⭐⭐

**Structure:**
- Single large problem with 3-5 sub-tasks
- Each sub-task builds on previous
- Progressive difficulty (easy → medium → hard)
- Total: 70 minutes for entire problem

**Example for BNSF AI Engineer role:**

```
TASK: Railroad Predictive Maintenance System

You are building a predictive maintenance system for BNSF locomotives.
Given sensor data from trains, implement the following:

Part 1 (15 min - Easy):
Write a function to clean sensor data:
- Remove null values
- Handle outliers (values > 3 standard deviations)
- Return cleaned dataset

Part 2 (20 min - Medium):
Implement anomaly detection:
- Calculate rolling 7-day average for each train
- Flag trains where current reading > 2x rolling average
- Return list of flagged trains with anomaly scores

Part 3 (20 min - Medium-Hard):
Build a simple predictive model:
- Features: sensor_reading, days_since_maintenance, train_age
- Target: needs_maintenance (0/1)
- Train a classifier (RandomForest or LogisticRegression)
- Return model and accuracy score

Part 4 (15 min - Hard):
Optimize the pipeline:
- Process dataset of 1 million rows efficiently
- Ensure O(n) or O(n log n) time complexity
- Handle edge cases (all nulls, single data point, etc.)

Constraints:
- Input size: up to 10^6 rows
- Time limit: 5 seconds per test case
- Memory limit: 512 MB
```

**Why this is likely:**
- Matches "AI Engineer" role (data + ML pipeline)
- Tests multiple skills in one cohesive problem
- Common for senior roles (you have 7+ years)
- Allows comprehensive evaluation

---

### **SCENARIO B: One Deep Technical Problem (30% probability)** ⭐

**Structure:**
- Single complex algorithm problem
- Very difficult (LeetCode Hard level)
- Multiple test cases with edge cases
- 70 minutes to solve optimally

**Example:**

```
TASK: Train Scheduling Optimization

BNSF needs to optimize train schedules across routes.

Given:
- routes = [(start_station, end_station, distance, priority)]
- trains = [(train_id, capacity, current_location)]
- deliveries = [(cargo_id, pickup_station, delivery_station, weight, deadline)]

Find the optimal assignment of deliveries to trains that:
1. Maximizes on-time deliveries (before deadline)
2. Minimizes total distance traveled
3. Respects train capacity constraints

Return: List of (train_id, [delivery_ids]) assignments

Constraints:
- 1 <= routes <= 10^5
- 1 <= trains <= 1000
- 1 <= deliveries <= 10^4
- Must run in O(n log n) time
```

**Why this is less likely:**
- Very hard for 70 minutes
- Doesn't test ML/AI skills directly
- More typical for Algorithm Engineer roles

---

## 🎯 MOST LIKELY: SCENARIO A (Multi-Part Data/ML Problem)

**Based on BNSF AI Engineer II role requirements, expect:**

### **Part 1: Data Cleaning & Preprocessing (20 min)**

**What they'll test:**
- Handling missing values (None, NaN)
- Detecting outliers
- Data validation
- Pandas/NumPy operations

**Example:**

```python
def clean_sensor_data(readings, timestamps):
    """
    Clean sensor data from locomotive sensors.
    
    Args:
        readings: List of float values (may contain None)
        timestamps: List of datetime strings
    
    Returns:
        dict with:
            'cleaned_readings': List of cleaned values
            'outlier_indices': List of indices where outliers were found
            'fill_strategy': String describing what you did
    
    Rules:
    - Replace None with median of previous 5 non-null values
    - Flag outliers as values > 3 standard deviations from mean
    - Handle edge cases (all None, < 5 values, etc.)
    """
    
    import numpy as np
    from statistics import median, stdev, mean
    
    # Your solution here
    pass
```

**Key concepts to know:**
- `pandas.fillna()`, `pandas.dropna()`
- `numpy.nanmedian()`, `numpy.nanmean()`
- Standard deviation: `numpy.std()`
- Rolling windows: `pandas.rolling()`

---

### **Part 2: Feature Engineering (15 min)**

**What they'll test:**
- Creating features from raw data
- Time-based aggregations
- Domain knowledge application

**Example:**

```python
def engineer_features(sensor_df):
    """
    Create features for predictive maintenance model.
    
    Args:
        sensor_df: DataFrame with columns:
            - train_id
            - timestamp
            - temperature
            - vibration
            - days_since_maintenance
    
    Returns:
        DataFrame with additional features:
            - rolling_7day_avg_temp
            - temp_change_rate
            - vibration_spike (binary: 1 if > threshold)
            - maintenance_urgency_score
    """
    
    import pandas as pd
    
    # Your solution here
    pass
```

**Key concepts:**
- `groupby()` operations
- `rolling()` windows
- Creating derived features
- Feature scaling/normalization

---

### **Part 3: Simple ML Model (20 min)**

**What they'll test:**
- Basic sklearn usage
- Train-test split
- Model training and evaluation
- Understanding metrics

**Example:**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

def build_maintenance_predictor(X, y):
    """
    Build a binary classifier for predictive maintenance.
    
    Args:
        X: Feature matrix (numpy array or pandas DataFrame)
        y: Target labels (0 = no maintenance, 1 = needs maintenance)
    
    Returns:
        dict with:
            'model': Trained model
            'precision': Precision score on test set
            'recall': Recall score on test set
            'f1': F1 score on test set
    
    Requirements:
    - Use 80-20 train-test split
    - Use RandomForestClassifier with 100 trees
    - Return metrics on test set
    """
    
    # Your solution here
    pass
```

**Key concepts:**
- `train_test_split(X, y, test_size=0.2)`
- `model.fit(X_train, y_train)`
- `model.predict(X_test)`
- Evaluation metrics (precision, recall, F1)

---

### **Part 4: Optimization & Edge Cases (15 min)**

**What they'll test:**
- Efficient algorithms (O(n) not O(n²))
- Handling large datasets
- Edge case handling

**Example:**

```python
def process_large_dataset(sensor_data):
    """
    Process 1 million sensor readings efficiently.
    
    Args:
        sensor_data: List of dicts, each with:
            - train_id
            - reading
            - timestamp
    
    Returns:
        dict mapping train_id to:
            - average_reading
            - max_reading
            - anomaly_count (readings > 3 std devs)
    
    Constraints:
    - Must handle up to 10^6 records
    - Time limit: 5 seconds
    - Memory limit: 512 MB
    
    Edge cases to handle:
    - Empty dataset
    - Single train
    - All readings are None
    - All readings are identical
    """
    
    from collections import defaultdict
    import numpy as np
    
    # Your solution here - must be O(n) time complexity
    pass
```

**Key concepts:**
- Use defaultdict/Counter (O(1) lookups)
- Single pass algorithms (avoid nested loops)
- Vectorized operations (NumPy)
- Generator expressions for memory efficiency

---

## 📚 3-DAY FOCUSED PREP PLAN (FEB 22-24)

### **DAY 1 (FEB 22 - TODAY): DATA CLEANING & PANDAS**

**4 hours:**

**Hour 1: Pandas Operations**
```python
import pandas as pd
import numpy as np

# Practice these:

# 1. Handling missing values
df.fillna(df.median())
df.fillna(method='ffill')  # forward fill
df.dropna(subset=['col1'])

# 2. Outlier detection
mean = df['value'].mean()
std = df['value'].std()
outliers = df[np.abs(df['value'] - mean) > 3*std]

# 3. Rolling windows
df['rolling_avg'] = df.groupby('id')['value'].rolling(7).mean().reset_index(0, drop=True)

# 4. GroupBy aggregations
df.groupby('train_id').agg({
    'temperature': ['mean', 'max', 'std'],
    'vibration': 'count'
})
```

**Hour 2-3: LeetCode Data Problems (5 problems)**
- 448. Find All Numbers Disappeared in Array (missing data)
- 283. Move Zeroes (data cleaning)
- 1656. Design an Ordered Stream (streaming data)
- 2574. Left and Right Sum Differences (aggregations)
- 2373. Largest Local Values in Matrix (rolling windows)

**Hour 4: Write Practice Solutions**
- Implement clean_sensor_data() function
- Practice handling edge cases
- Time yourself (20 min per problem)

---

### **DAY 2 (FEB 23 - TOMORROW): ML BASICS & SKLEARN**

**4 hours:**

**Hour 1: Sklearn Review**
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, 
    recall_score, f1_score, 
    confusion_matrix, classification_report
)

# Practice workflow:

# 1. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Train model
model = RandomForestClassifier(
    n_estimators=100, 
    random_state=42,
    max_depth=10
)
model.fit(X_train, y_train)

# 3. Predict
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)  # probabilities

# 4. Evaluate
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(classification_report(y_test, y_pred))

# 5. Feature importance
importances = model.feature_importances_
```

**Hour 2: Feature Engineering Practice**
```python
# Common patterns for BNSF:

# Time-based features
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

# Lag features
df['prev_reading'] = df.groupby('train_id')['reading'].shift(1)
df['reading_change'] = df['reading'] - df['prev_reading']

# Aggregated features
df['avg_last_7days'] = df.groupby('train_id')['reading'].rolling(7).mean()

# Binary flags
df['high_temp'] = (df['temperature'] > 80).astype(int)
df['needs_attention'] = ((df['vibration'] > threshold) | 
                          (df['days_since_maint'] > 30)).astype(int)
```

**Hour 3-4: Kaggle Mini-Projects**
- Find "Predictive Maintenance" datasets on Kaggle
- Practice end-to-end ML pipeline
- Focus on speed (complete in 30-40 min)

---

### **DAY 3 (FEB 24 - MONDAY): ALGORITHMS & OPTIMIZATION**

**4 hours:**

**Hour 1: Time Complexity Review**
```python
# O(1) - Constant
def get_first(arr):
    return arr[0] if arr else None

# O(n) - Linear (GOOD for Codility)
def find_max(arr):
    return max(arr)

# O(n log n) - Linearithmic (ACCEPTABLE)
def sort_data(arr):
    return sorted(arr)

# O(n²) - Quadratic (AVOID for large datasets)
def find_pairs(arr):  # BAD
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs

# Use hash maps instead:
def find_pairs_efficient(arr):  # GOOD
    seen = set()
    pairs = []
    for num in arr:
        if target - num in seen:
            pairs.append((num, target - num))
        seen.add(num)
    return pairs
```

**Hour 2: Efficient Data Structures**
```python
from collections import defaultdict, Counter, deque

# Use defaultdict for grouping
train_data = defaultdict(list)
for reading in sensor_data:
    train_data[reading['train_id']].append(reading['value'])

# Use Counter for frequency
from collections import Counter
freq = Counter(values)
most_common = freq.most_common(5)  # top 5

# Use sets for O(1) lookups
seen = set()
if value in seen:  # O(1) lookup
    # do something
seen.add(value)
```

**Hour 3-4: Mock Assessment**
- Create 1 large multi-part problem
- Time yourself: 70 minutes
- Simulate real conditions
- Review solution after

---

## 🎯 PRACTICE PROBLEMS FOR BNSF

**Do these EXACT problems (most similar to what you'll see):**

### **Data Cleaning:**
1. LeetCode 283: Move Zeroes
2. LeetCode 448: Find Disappeared Numbers
3. LeetCode 26: Remove Duplicates from Sorted Array

### **Aggregations:**
4. LeetCode 2574: Left and Right Sum Differences
5. LeetCode 1920: Build Array from Permutation
6. LeetCode 2433: Find The Original Array of Prefix Xor

### **Optimization:**
7. LeetCode 1: Two Sum (hash map optimization)
8. LeetCode 217: Contains Duplicate (set usage)
9. LeetCode 53: Maximum Subarray (Kadane's algorithm)

---

## 🚨 CODILITY-SPECIFIC TIPS

### **1. Read the problem 3 times**
- First: Get general idea
- Second: Understand constraints
- Third: Identify edge cases

### **2. Plan before coding (5 min)**
```python
# Write pseudocode as comments first:

def solve(data):
    # Step 1: Clean data (remove nulls, outliers)
    # Step 2: Calculate rolling average
    # Step 3: Flag anomalies
    # Step 4: Return results
    
    # Then implement each step
    pass
```

### **3. Test with examples**
```python
# Always test these edge cases:

# Empty input
assert solve([]) == expected

# Single element
assert solve([5]) == expected

# All same values
assert solve([1,1,1,1]) == expected

# All different
assert solve([1,2,3,4]) == expected

# With nulls
assert solve([1, None, 3]) == expected

# Large dataset (performance test)
assert solve(list(range(10**6))) == expected
```

### **4. Use descriptive variable names**
```python
# GOOD:
cleaned_readings = [r for r in readings if r is not None]
rolling_avg = calculate_rolling_average(cleaned_readings, window=7)

# BAD:
cr = [r for r in rd if r]
ra = calc(cr, 7)
```

### **5. Write helper functions**
```python
def solve_main_problem(data):
    # Main solution
    cleaned = clean_data(data)
    features = engineer_features(cleaned)
    model = train_model(features)
    return model

def clean_data(data):
    # Separate function for clarity
    pass

def engineer_features(data):
    # Separate function
    pass
```

---

## 💪 YOU'RE VERY WELL PREPARED

**Why you'll succeed:**

**1. You have 3 full days of focused prep** ✅
- Feb 22: Data cleaning + Pandas
- Feb 23: ML + sklearn
- Feb 24: Optimization + mock test

**2. You're overqualified** ✅
- They want 3+ years, you have 7+
- You've built production ML pipelines
- 400TB data experience >> any Codility problem

**3. You know the stack** ✅
- Python: Expert
- Pandas/NumPy: Daily use
- Sklearn: Production experience
- AWS/Databricks: Broadcom work

**4. You have CTO referral** ✅
- Ashwin wants you to succeed
- Higher tolerance for "good enough" score

---

## 🎯 EXPECTED SCORE

**With 3 days of focused prep:**

**Your expected score: 85-95 points** ✅

**Breakdown:**
- Part 1 (Data cleaning): 95% (easy for you)
- Part 2 (Feature engineering): 90% (your daily work)
- Part 3 (ML model): 85% (sklearn basics)
- Part 4 (Optimization): 80% (need to practice)

**Passing threshold: ~70 points**

**You'll COMFORTABLY pass** 🎉

---

## ✅ YOUR 3-DAY PLAN

**TODAY (FEB 22): Data cleaning + Pandas** (4 hours)
**TOMORROW (FEB 23): ML + sklearn** (4 hours)
**MONDAY (FEB 24): Optimization + mock** (4 hours)
**TUESDAY (FEB 25): TAKE TEST 10 AM** ⚡

---

**START TODAY'S PREP NOW** 📚

**YOU'RE GOING TO CRUSH THIS!** 💪🚀

Let me know if you need help with any specific concepts! 🎯
