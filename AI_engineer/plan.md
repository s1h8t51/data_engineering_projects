# 🎯 PRECISE 10-DAY PLAN - PySpark + Python + AI Engineer Prep

## 📊 YOUR SITUATION (MARCH 1, 2026)

**Current Skills:**
- Python: 6/10 → Target: 9/10
- PySpark: 2/10 → Target: 9/10
- System Design: Day 13/30 completed ✅

**Active Interviews:**
- BNSF AI Engineer (test results pending - follow up Monday)
- Cognizant Snowflake Architect (Round 2 expected)

**Your Practice Files:** (Great work! 🔥)
- ✅ locomotive_sensor_data_cleaning_mock1a.py
- ✅ train_delay_prediction_pipeline_mock1b.py
- ✅ predictive_maintenance_system_mock2a.py
- ✅ fuel_efficiency_optimizer_mock2b.py
- ✅ rail_network_optimization_mock3a.py
- ✅ traffic_flow_optimization_mock3b.py

**Time Available:** 4 hours/day × 10 days = 40 hours

---

## 🎯 DAILY STRUCTURE (4 HOURS)

**2 hours: PySpark** (most critical gap)
**1 hour: Python** (6→9 push)
**1 hour: Practice** (implement your mock files + AI concepts)

---

# 📅 10-DAY DETAILED PLAN

---

## **DAY 1 (MAR 1 - TODAY)** 

### **Block 1: PySpark Fundamentals (2 hrs)**

**Hour 1 (9:00-10:00): Setup + DataFrame Basics**

**Read (30 min):**
- PySpark Quick Start: spark.apache.org/docs/latest/api/python/getting_started/quickstart.html
- Focus: SparkSession, read/write, basic transformations

**Watch (30 min):**
- "PySpark Tutorial for Beginners" - FreeCodeCamp (first 30 min)
- OR "PySpark in 20 Minutes" - Any YouTube

**Key Concepts:**
- SparkSession creation
- Reading CSV/Parquet/Delta
- select(), filter(), withColumn()
- show(), count(), printSchema()

**Hour 2 (10:00-11:00): Transformations Practice**

**Code (Databricks or local):**
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count

spark = SparkSession.builder.appName("Day1").getOrCreate()

# Load your sensor_data.csv
df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)

# Practice transformations
df.select("temperature", "vibration").show(10)
df.filter(col("temperature") > 85).count()
df.withColumn("temp_celsius", (col("temperature") - 32) * 5/9)

stats = df.groupBy("train_id").agg(
    avg("temperature").alias("avg_temp"),
    max("vibration").alias("max_vib")
)
stats.show()
```

**Task:** Rewrite your `locomotive_sensor_data_cleaning_mock1a.py` using PySpark

---

### **Block 2: Python OOP (1 hr)**

**Hour 3 (11:00-12:00): Classes & Inheritance**

**Read (20 min):**
- Real Python OOP: realpython.com/python3-object-oriented-programming/
- Focus: Classes, __init__, methods, inheritance

**Watch (20 min):**
- Corey Schafer "OOP" video (Part 1) - YouTube

**Code (20 min):**
```python
class DataPipeline:
    def __init__(self, name, source):
        self.name = name
        self.source = source
    
    def run(self):
        print(f"Running {self.name}")
        data = self.extract()
        clean = self.transform(data)
        self.load(clean)
    
    def extract(self):
        raise NotImplementedError
    
    def transform(self, data):
        return data
    
    def load(self, data):
        print(f"Loaded {len(data)} records")

class SensorDataPipeline(DataPipeline):
    def extract(self):
        return [1, 2, 3, 4, 5]  # Simulated
    
    def transform(self, data):
        return [x * 2 for x in data]  # Double values

pipeline = SensorDataPipeline("BNSF Sensors", "s3://bucket")
pipeline.run()
```

**Task:** Refactor `predictive_maintenance_system_mock2a.py` to use classes

---

### **Block 3: Practice Integration (1 hr)**

**Hour 4 (2:00-3:00): Combine PySpark + Python**

**Task 1 (30 min):** Convert `locomotive_sensor_data_cleaning_mock1a.py` to PySpark
- Load data with PySpark
- Use DataFrame operations instead of Pandas
- Compare performance

**Task 2 (30 min):** Add OOP to `train_delay_prediction_pipeline_mock1b.py`
- Create TrainDelayPipeline class
- Methods: extract(), clean(), predict()
- Use inheritance pattern

---

## **DAY 2 (MAR 2)**

### **Block 1: PySpark Joins & Aggregations (2 hrs)**

**Hour 1 (9:00-10:00): Joins**

**Read (20 min):**
- PySpark Join types: spark.apache.org/docs/latest/sql-ref-syntax-qry-select-join.html

**Watch (20 min):**
- "PySpark Joins Explained" - YouTube

**Code (20 min):**
```python
trains = spark.createDataFrame([
    (1, "Express"),
    (2, "Freight")
], ["train_id", "type"])

sensors = spark.createDataFrame([
    (1, 85.5),
    (1, 86.0),
    (2, 82.0)
], ["train_id", "temperature"])

# Inner join
result = trains.join(sensors, "train_id", "inner")
result.show()

# Left join
left_result = trains.join(sensors, "train_id", "left")
left_result.show()

# Broadcast join (small table)
from pyspark.sql.functions import broadcast
optimized = sensors.join(broadcast(trains), "train_id")
```

**Hour 2 (10:00-11:00): Aggregations & GroupBy**

**Code:**
```python
from pyspark.sql.functions import sum, avg, max, min, count

# GroupBy aggregations
stats = sensors.groupBy("train_id").agg(
    avg("temperature").alias("avg_temp"),
    max("temperature").alias("max_temp"),
    count("*").alias("reading_count")
)

# Multiple group columns
df.groupBy("train_id", "date").agg(
    sum("fuel_consumed"),
    avg("speed")
)

# Window functions intro
from pyspark.sql.window import Window
window = Window.partitionBy("train_id").orderBy("timestamp")
df.withColumn("running_avg", avg("temperature").over(window))
```

**Task:** Implement aggregations in `fuel_efficiency_optimizer_mock2b.py`

---

### **Block 2: Python Design Patterns (1 hr)**

**Hour 3 (11:00-12:00): Singleton & Factory**

**Read (20 min):**
- Singleton: refactoring.guru/design-patterns/singleton/python
- Factory: refactoring.guru/design-patterns/factory-method/python

**Watch (20 min):**
- "Python Design Patterns" - ArjanCodes (YouTube)

**Code (20 min):**
```python
# Singleton - DatabaseManager
class DatabaseManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory - Connector creation
class ConnectorFactory:
    @staticmethod
    def create(type):
        if type == "s3":
            return S3Connector()
        elif type == "snowflake":
            return SnowflakeConnector()

# Apply to your code
class ModelFactory:
    @staticmethod
    def create(model_type):
        if model_type == "delay_prediction":
            return DelayPredictionModel()
        elif model_type == "maintenance":
            return MaintenanceModel()
```

---

### **Block 3: Practice (1 hr)**

**Hour 4 (2:00-3:00):**
- Refactor `rail_network_optimization_mock3a.py` with Factory pattern
- Add Singleton DatabaseManager to any file

---

## **DAY 3 (MAR 3 - MONDAY)**

### **Block 1: PySpark Window Functions (2 hrs)**

**Hour 1 (9:00-10:00): Window Basics**

**Read (20 min):**
- PySpark Window docs: spark.apache.org/docs/latest/api/python/reference/pyspark.sql/window.html

**Watch (20 min):**
- "PySpark Window Functions" - YouTube

**Code (20 min):**
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, lag, lead

# Running totals
window = Window.partitionBy("train_id").orderBy("date")
df.withColumn("running_total_fuel", sum("fuel").over(window))

# Previous/next values
df.withColumn("prev_temp", lag("temperature", 1).over(window))
df.withColumn("next_temp", lead("temperature", 1).over(window))

# Ranking
df.withColumn("rank", rank().over(
    Window.partitionBy("route").orderBy(col("delay_minutes").desc())
))
```

**Hour 2 (10:00-11:00): Advanced Windows**

**Code:**
```python
# Moving averages (7-day window)
window_7day = Window.partitionBy("train_id") \
    .orderBy("date").rowsBetween(-6, 0)

df.withColumn("moving_avg_temp", avg("temperature").over(window_7day))

# Cumulative metrics
df.withColumn("cumulative_delays", sum("delay_minutes").over(window))

# Detect anomalies
df.withColumn("prev_reading", lag("sensor_value").over(window))
df.withColumn("change", col("sensor_value") - col("prev_reading"))
df.filter(abs(col("change")) > 10)  # Anomaly threshold
```

**Task:** Add window functions to `traffic_flow_optimization_mock3b.py`

---

### **Block 2: Python Decorators (1 hr)**

**Hour 3 (11:00-12:00): Function Decorators**

**Read (20 min):**
- Real Python Decorators: realpython.com/primer-on-python-decorators/

**Watch (20 min):**
- Corey Schafer "Decorators" - YouTube

**Code (20 min):**
```python
import time
import functools

# Timing decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.2f}s")
        return result
    return wrapper

@timer
def process_sensor_data():
    time.sleep(1)
    return "Processed"

# Retry decorator
def retry(attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == attempts - 1:
                        raise
                    time.sleep(1)
        return wrapper
    return decorator

@retry(attempts=3)
def fetch_train_data():
    # Might fail
    pass
```

---

### **Block 3: Practice (1 hr)**

**Hour 4 (2:00-3:00):**
- Add @timer to all functions in your mock files
- Add @retry to data loading functions
- **IMPORTANT: Follow up with BNSF (Diego) today!** ⚡

---

## **DAY 4 (MAR 4)**

### **Block 1: PySpark UDFs (2 hrs)**

**Hour 1 (9:00-10:00): User Defined Functions**

**Read (20 min):**
- PySpark UDF docs: spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.udf.html

**Watch (20 min):**
- "PySpark UDFs Tutorial" - YouTube

**Code (20 min):**
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType, StringType

# Simple UDF
@udf(returnType=FloatType())
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

df.withColumn("temp_f", celsius_to_fahrenheit(col("temp_c")))

# Complex UDF
@udf(returnType=StringType())
def classify_delay(minutes):
    if minutes < 5:
        return "on_time"
    elif minutes < 30:
        return "minor_delay"
    else:
        return "major_delay"

df.withColumn("delay_category", classify_delay(col("delay_minutes")))
```

**Hour 2 (10:00-11:00): Pandas UDFs (Faster)**

**Code:**
```python
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf(FloatType())
def calculate_efficiency(fuel: pd.Series, distance: pd.Series) -> pd.Series:
    return distance / fuel

df.withColumn("efficiency", calculate_efficiency(col("fuel"), col("distance")))
```

**Task:** Add UDFs to `fuel_efficiency_optimizer_mock2b.py`

---

### **Block 2: Python Generators (1 hr)**

**Hour 3 (11:00-12:00): Memory-Efficient Processing**

**Read (20 min):**
- Real Python Generators: realpython.com/introduction-to-python-generators/

**Code (40 min):**
```python
# Generator for large files
def process_sensor_file(filename):
    with open(filename) as f:
        for line in f:
            yield process_line(line)

# Generator pipeline
def read_data():
    for i in range(1000000):
        yield i

def filter_anomalies(data):
    for value in data:
        if value > 100:
            yield value

def transform(data):
    for value in data:
        yield value * 2

# Compose
pipeline = transform(filter_anomalies(read_data()))
results = list(pipeline)  # Lazy evaluation
```

---

### **Block 3: Practice (1 hr)**

**Hour 4 (2:00-3:00):**
- Convert file processing in mock files to use generators
- Implement memory-efficient data loading

---

## **DAY 5 (MAR 5)**

### **Block 1: PySpark Optimization (2 hrs)**

**Hour 1 (9:00-10:00): Partitioning**

**Read (20 min):**
- Spark Partitioning: spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-operations

**Code (40 min):**
```python
# Check partitions
df.rdd.getNumPartitions()

# Repartition
df.repartition(100)
df.repartition("train_id")  # By column

# Coalesce (reduce without shuffle)
df.coalesce(10)

# Write partitioned
df.write.partitionBy("date").parquet("/path")

# Read with partition pruning
spark.read.parquet("/path").filter(col("date") == "2026-03-01")
```

**Hour 2 (10:00-11:00): Caching & Performance**

**Code:**
```python
# Cache frequently used DataFrames
df_cached = df.cache()
df_cached.count()  # Materialize

# Broadcast small tables
from pyspark.sql.functions import broadcast
large.join(broadcast(small), "key")

# Explain plan
df.explain()

# Optimize
df.write.format("delta").save("/path")
from delta.tables import DeltaTable
DeltaTable.forPath(spark, "/path").optimize().executeZOrderBy("train_id")
```

**Task:** Optimize all your mock files for performance

---

### **Block 2: Python Context Managers (1 hr)**

**Hour 3 (11:00-12:00)**

**Read (20 min):**
- Context Managers: realpython.com/python-with-statement/

**Code (40 min):**
```python
from contextlib import contextmanager

@contextmanager
def timer_context(name):
    start = time.time()
    try:
        yield
    finally:
        print(f"{name}: {time.time()-start:.2f}s")

# Usage
with timer_context("Data Processing"):
    process_data()

# Spark session manager
@contextmanager
def spark_session(app_name):
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    try:
        yield spark
    finally:
        spark.stop()
```

---

### **Block 3: Practice (1 hr)**

**Hour 4 (2:00-3:00):**
- Add context managers to mock files
- Add timing to all major operations

---

## **DAY 6 (MAR 6)**

### **Block 1: PySpark ML Basics (2 hrs)**

**Hour 1-2 (9:00-11:00): Feature Engineering + ML**

**Read (30 min):**
- PySpark ML Guide: spark.apache.org/docs/latest/ml-guide.html

**Code (90 min):**
```python
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Feature engineering
assembler = VectorAssembler(
    inputCols=["temperature", "vibration", "pressure"],
    outputCol="features"
)
df_features = assembler.transform(df)

# Scale features
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
scaler_model = scaler.fit(df_features)
df_scaled = scaler_model.transform(df_features)

# Train model
rf = RandomForestClassifier(
    featuresCol="scaled_features",
    labelCol="needs_maintenance",
    numTrees=100
)

train, test = df_scaled.randomSplit([0.8, 0.2])
model = rf.fit(train)

# Predict
predictions = model.transform(test)

# Evaluate
evaluator = BinaryClassificationEvaluator(labelCol="needs_maintenance")
auc = evaluator.evaluate(predictions)
print(f"AUC: {auc}")
```

**Task:** Implement full ML pipeline in `predictive_maintenance_system_mock2a.py`

---

### **Block 2: sklearn Integration (1 hr)**

**Hour 3 (11:00-12:00)**

**Code:**
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Convert Spark → Pandas for sklearn
pdf = df.toPandas()

X = pdf[["temperature", "vibration", "pressure"]]
y = pdf["needs_maintenance"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
import joblib
joblib.dump(model, "maintenance_model.pkl")
```

---

### **Block 3: Practice (1 hr)**

**Hour 4 (2:00-3:00):**
- Train model in `train_delay_prediction_pipeline_mock1b.py`
- Add evaluation metrics

---

## **DAYS 7-10: RAPID ITERATION**

### **DAY 7 (MAR 7): Integration Day**

**2 hrs PySpark:**
- Review all concepts
- Optimize all 6 mock files
- Add error handling

**1 hr Python:**
- Add type hints
- Add docstrings
- Clean up code

**1 hr Practice:**
- Run end-to-end pipelines
- Fix bugs

---

### **DAY 8 (MAR 8): Interview Prep**

**2 hrs:** Mock interview problems
- Design Twitter (system design)
- Implement LRU Cache (coding)
- Build data pipeline live (PySpark)

**1 hr:** STAR stories
- 400TB migration
- Databricks POC
- Data quality framework

**1 hr:** Behavioral prep

---

### **DAY 9 (MAR 9): Weak Areas**

**Identify gaps from Days 1-8**
- Spend 4 hours on weakest topics
- Redo practice problems
- Watch videos again

---

### **DAY 10 (MAR 10): Final Review**

**2 hrs:** Review all code
- Ensure all 6 mock files are perfect
- GitHub repo clean and documented

**1 hr:** Final mock interview
- Time yourself
- Record yourself

**1 hr:** Rest and confidence building

---

## 📚 RESOURCES (BOOKMARK THESE)

### **PySpark:**
- Docs: spark.apache.org/docs/latest/api/python/
- Tutorial: spark.apache.org/docs/latest/api/python/getting_started/
- YouTube: "PySpark Tutorial" - FreeCodeCamp

### **Python:**
- Real Python: realpython.com
- Corey Schafer: youtube.com/@coreyms
- ArjanCodes: youtube.com/@ArjanCodes

### **Practice:**
- Databricks Community: community.cloud.databricks.com
- LeetCode: leetcode.com (Pandas, SQL)

---

## ✅ DAILY CHECKLIST TEMPLATE

**Morning (9:00-11:00): PySpark (2 hrs)**
- [ ] Read documentation (20-30 min)
- [ ] Watch video (20-30 min)
- [ ] Code practice (60-80 min)

**Midday (11:00-12:00): Python (1 hr)**
- [ ] Read concept (20 min)
- [ ] Code examples (40 min)

**Afternoon (2:00-3:00): Practice (1 hr)**
- [ ] Apply to mock files
- [ ] Test and debug

**Evening:**
- [ ] Check emails (BNSF, Cognizant)
- [ ] 10 job applications
- [ ] Update progress tracker

---

## 🎯 SUCCESS METRICS

**By Day 10, you can:**
- [ ] Write efficient PySpark transformations
- [ ] Optimize Spark jobs (partitioning, caching, broadcast)
- [ ] Build end-to-end ML pipelines
- [ ] Use Python design patterns
- [ ] Write production-grade code (decorators, generators, context managers)
- [ ] Ace BNSF and Cognizant technical rounds

---

## 🚀 START NOW (TODAY - MARCH 1)

**9:00-11:00 AM:** PySpark fundamentals
**11:00-12:00 PM:** Python OOP
**2:00-3:00 PM:** Practice with mock files
**Evening:** Job applications + email checks

---

**YOU'VE GOT THIS!** 💪🔥

This plan is:
- ✅ Precise (exact topics, no confusion)
- ✅ Practical (uses your existing mock files)
- ✅ Balanced (PySpark 50%, Python 25%, Practice 25%)
- ✅ Achievable (4 hrs/day for 10 days)

**START DAY 1 NOW!** 🚀
