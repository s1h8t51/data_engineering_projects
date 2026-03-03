# 🎯 5-DAY INTENSIVE: PySpark (Beginner→Intermediate) + Python (Intermediate→Advanced) + Databricks

## 📊 YOUR CURRENT STATE & GOAL

**Current Level:**
- Python: Intermediate (6/10) → Target: Advanced (8/10)
- PySpark: Beginner (2/10) → Target: Intermediate (6/10)
- Databricks: Beginner (1/10) → Target: Intermediate (5/10)

**Focus:** Real-world migration project scenarios (like your 400TB migration)

**Time:** 4 hours/day × 5 days = 20 hours total

---

## ⏰ DAILY STRUCTURE (4 HOURS)

**Hour 1 (9:00-10:00): Learn Concepts** 📚
- Read documentation
- Watch short videos (10-15 min)
- Understand theory

**Hour 2 (10:00-11:00): Hands-on Practice** 💻
- Code in Databricks
- Follow tutorials
- Build small examples

**Hour 3 (11:00-12:00): Real Migration Task** 🏗️
- 30-min timed coding challenge
- Real-world scenario
- Complete working solution

**Hour 4 (2:00-3:00): Review & Advanced** 🚀
- Debug your code
- Optimize performance
- Add production features

---

# 📅 DAY 1 (MARCH 3) - DATABRICKS SETUP + PYSPARK BASICS

## **Hour 1 (9:00-10:00): Setup & Fundamentals**

### **Tasks:**

**1. Databricks Setup (15 min):**
```
1. Login: community.cloud.databricks.com
2. Create Cluster:
   - Click "Compute" → "Create Cluster"
   - Name: "learning-cluster"
   - Runtime: 12.2 LTS (includes Spark 3.3.2)
   - Node type: Single node (for learning)
   - Click "Create Cluster"
3. Wait 3-5 minutes for cluster to start
```

**2. Read PySpark Basics (25 min):**
- Databricks docs: "Apache Spark on Databricks"
- Understand: DataFrame, lazy evaluation, actions vs transformations

**3. Watch Video (20 min):**
- "PySpark Tutorial for Beginners" (YouTube - first 20 min)

---

## **Hour 2 (10:00-11:00): First Databricks Notebook**

### **Create New Notebook:**

**File → New → Notebook**
- Name: "Day1_PySpark_Basics"
- Language: Python
- Cluster: learning-cluster

### **Practice Code (Copy & Run Each Cell):**

```python
# CELL 1: Create SparkSession (auto-created in Databricks)
print(f"Spark version: {spark.version}")
print(f"Available cores: {spark.sparkContext.defaultParallelism}")

# CELL 2: Create sample data (like sensor data)
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, TimestampType
from datetime import datetime

# Define schema (production best practice)
schema = StructType([
    StructField("train_id", StringType(), False),
    StructField("sensor_id", IntegerType(), False),
    StructField("temperature", FloatType(), True),
    StructField("vibration", FloatType(), True),
    StructField("timestamp", TimestampType(), True)
])

# Create sample data
data = [
    ("TRAIN_001", 1, 85.5, 2.3, datetime(2026, 3, 1, 10, 0)),
    ("TRAIN_001", 2, 86.2, 2.1, datetime(2026, 3, 1, 10, 5)),
    ("TRAIN_002", 1, 82.1, 3.5, datetime(2026, 3, 1, 10, 0)),
    ("TRAIN_002", 2, 83.4, 3.2, datetime(2026, 3, 1, 10, 5)),
    ("TRAIN_001", 1, 90.1, 5.8, datetime(2026, 3, 1, 10, 10))  # Anomaly!
]

df = spark.createDataFrame(data, schema)

# CELL 3: Basic operations
df.show()
df.printSchema()
print(f"Total records: {df.count()}")

# CELL 4: Select columns
df.select("train_id", "temperature").show()

# CELL 5: Filter (WHERE clause)
df.filter(df.temperature > 85).show()

# CELL 6: Add new column
from pyspark.sql.functions import col
df_celsius = df.withColumn("temp_celsius", (col("temperature") - 32) * 5/9)
df_celsius.show()

# CELL 7: Write to Delta (Databricks format)
df.write.format("delta").mode("overwrite").save("/tmp/day1_sensor_data")

# CELL 8: Read from Delta
df_read = spark.read.format("delta").load("/tmp/day1_sensor_data")
df_read.show()
```

---

## **Hour 3 (11:00-11:30): TIMED TASK (30 MIN)**

### **🏗️ REAL MIGRATION SCENARIO: CSV to Delta Conversion**

**Scenario:** You're migrating legacy CSV files to Delta Lake (like your 400TB migration)

**Task: Complete in 30 minutes**

```python
# CREATE NEW NOTEBOOK: "Day1_Migration_Task"

# TASK 1: Upload sample CSV (5 min)
# Create this CSV in local file first, then upload to Databricks
# Or use dbutils to create sample data

# CELL 1: Create sample CSV data
csv_data = """train_id,date,fuel_consumed,distance_km,avg_speed
TRAIN_001,2026-03-01,500.5,850.2,75.5
TRAIN_001,2026-03-02,510.3,820.5,72.1
TRAIN_002,2026-03-01,480.2,900.1,80.2
TRAIN_002,2026-03-02,495.8,880.3,78.5
TRAIN_003,2026-03-01,520.1,800.5,70.3"""

# Write to DBFS (Databricks File System)
dbutils.fs.put("/tmp/legacy_fuel_data.csv", csv_data, True)

# TASK 2: Read CSV with schema inference (5 min)
# YOUR CODE HERE:
df_csv = spark.read.csv("/tmp/legacy_fuel_data.csv", header=True, inferSchema=True)
df_csv.show()
df_csv.printSchema()

# TASK 3: Data quality checks (10 min)
# 1. Check for nulls
# 2. Validate fuel_consumed > 0
# 3. Calculate fuel efficiency (km per liter)
# YOUR CODE HERE:
from pyspark.sql.functions import col, when, isnan, isnull

# Check nulls
null_counts = df_csv.select([
    sum(when(isnull(c), 1).otherwise(0)).alias(c) 
    for c in df_csv.columns
])
null_counts.show()

# Validate fuel > 0
df_validated = df_csv.filter(col("fuel_consumed") > 0)
print(f"Valid records: {df_validated.count()}/{df_csv.count()}")

# Calculate efficiency
df_enriched = df_validated.withColumn(
    "efficiency_km_per_liter", 
    col("distance_km") / col("fuel_consumed")
)
df_enriched.show()

# TASK 4: Write to Delta with partitioning (10 min)
# Partition by train_id for query optimization
# YOUR CODE HERE:
df_enriched.write \
    .format("delta") \
    .mode("overwrite") \
    .partitionBy("train_id") \
    .save("/tmp/delta/fuel_efficiency")

# Verify
df_delta = spark.read.format("delta").load("/tmp/delta/fuel_efficiency")
print(f"Delta table records: {df_delta.count()}")
df_delta.show()

# TASK 5: Query optimization check
# Show partitions created
display(dbutils.fs.ls("/tmp/delta/fuel_efficiency"))
```

**✅ Success Criteria:**
- [ ] CSV loaded successfully
- [ ] Null checks implemented
- [ ] Fuel efficiency calculated
- [ ] Delta table created with partitions
- [ ] Completed in 30 minutes

---

## **Hour 4 (2:00-3:00): Review & Python Advanced**

### **Review Migration Task:**
- Did you finish in 30 min?
- What was hardest?
- Optimize your code

### **Python Advanced Topic: List Comprehensions & Lambda**

```python
# CELL 1: List comprehensions (Python optimization)
# Instead of loops, use comprehensions

# Bad (slow)
squares = []
for i in range(1000000):
    squares.append(i**2)

# Good (fast)
squares = [i**2 for i in range(1000000)]

# With filter
evens = [i for i in range(100) if i % 2 == 0]

# CELL 2: Lambda functions
# Anonymous functions for PySpark

from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType

# Define UDF using lambda
celsius_to_fahrenheit = udf(lambda c: c * 9/5 + 32, FloatType())

# Use in DataFrame
df_temp = spark.createDataFrame([(20.0,), (25.0,), (30.0,)], ["celsius"])
df_temp.withColumn("fahrenheit", celsius_to_fahrenheit("celsius")).show()

# CELL 3: Map, Filter, Reduce (functional programming)
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map (transform each element)
squared = list(map(lambda x: x**2, numbers))

# Filter (select elements)
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce (aggregate)
sum_all = reduce(lambda x, y: x + y, numbers)

print(f"Squared: {squared}")
print(f"Evens: {evens}")
print(f"Sum: {sum_all}")
```

---

# 📅 DAY 2 (MARCH 4) - PYSPARK TRANSFORMATIONS + PYTHON OOP

## **Hour 1 (9:00-10:00): PySpark Joins & Aggregations**

### **Read (20 min):**
- PySpark SQL Guide: "Joins"
- PySpark SQL Guide: "Aggregations"

### **Watch (20 min):**
- "PySpark Joins Explained" (YouTube)

### **Key Concepts:**
- Inner, Left, Right, Outer joins
- Broadcast joins (optimization)
- GroupBy aggregations
- Window functions intro

---

## **Hour 2 (10:00-11:00): Practice Joins**

```python
# CREATE NOTEBOOK: "Day2_Joins_Aggregations"

# CELL 1: Create dimension and fact tables (like your migration project)
from pyspark.sql import Row

# Dimension: Train metadata
trains = spark.createDataFrame([
    Row(train_id="TRAIN_001", model="Freight-X200", capacity_tons=5000),
    Row(train_id="TRAIN_002", model="Express-E150", capacity_tons=3000),
    Row(train_id="TRAIN_003", model="Freight-X200", capacity_tons=5000)
])

# Fact: Daily operations
operations = spark.createDataFrame([
    Row(train_id="TRAIN_001", date="2026-03-01", cargo_tons=4500, revenue=15000),
    Row(train_id="TRAIN_001", date="2026-03-02", cargo_tons=4800, revenue=16000),
    Row(train_id="TRAIN_002", date="2026-03-01", cargo_tons=2800, revenue=12000),
    Row(train_id="TRAIN_004", date="2026-03-01", cargo_tons=3000, revenue=13000)  # Orphan!
])

trains.show()
operations.show()

# CELL 2: Inner Join (only matching records)
inner_result = trains.join(operations, "train_id", "inner")
print(f"Inner join: {inner_result.count()} records")
inner_result.show()

# CELL 3: Left Join (all trains, even without operations)
left_result = trains.join(operations, "train_id", "left")
print(f"Left join: {left_result.count()} records")
left_result.show()

# CELL 4: Broadcast Join (optimization for small tables)
from pyspark.sql.functions import broadcast

# When one table is small (< 10MB), broadcast it
optimized_join = operations.join(broadcast(trains), "train_id", "inner")
optimized_join.show()

# CELL 5: Aggregations
from pyspark.sql.functions import sum, avg, count, max

# Total revenue per train
revenue_by_train = operations.groupBy("train_id").agg(
    sum("revenue").alias("total_revenue"),
    avg("cargo_tons").alias("avg_cargo"),
    count("*").alias("num_trips")
)
revenue_by_train.show()

# CELL 6: Join + Aggregate (common pattern)
train_performance = trains.join(operations, "train_id", "inner") \
    .groupBy("model") \
    .agg(
        sum("revenue").alias("total_revenue"),
        avg("cargo_tons").alias("avg_cargo")
    )
train_performance.show()
```

---

## **Hour 3 (11:00-11:30): TIMED TASK (30 MIN)**

### **🏗️ MIGRATION SCENARIO: Data Warehouse Star Schema Join**

**Scenario:** You're joining dimension and fact tables from legacy Oracle to Databricks

```python
# CREATE NOTEBOOK: "Day2_Migration_Task"

# SETUP: Create sample tables (5 min)
# Dimension: Customers
customers = spark.createDataFrame([
    Row(customer_id=1, name="ABC Corp", industry="Manufacturing"),
    Row(customer_id=2, name="XYZ Inc", industry="Retail"),
    Row(customer_id=3, name="DEF Ltd", industry="Technology")
])

# Dimension: Products
products = spark.createDataFrame([
    Row(product_id=101, name="Widget-A", category="Hardware"),
    Row(product_id=102, name="Widget-B", category="Software"),
    Row(product_id=103, name="Widget-C", category="Hardware")
])

# Fact: Sales transactions
sales = spark.createDataFrame([
    Row(sale_id=1, customer_id=1, product_id=101, quantity=100, amount=5000.0, sale_date="2026-03-01"),
    Row(sale_id=2, customer_id=1, product_id=102, quantity=50, amount=7500.0, sale_date="2026-03-01"),
    Row(sale_id=3, customer_id=2, product_id=101, quantity=200, amount=10000.0, sale_date="2026-03-02"),
    Row(sale_id=4, customer_id=3, product_id=103, quantity=150, amount=8000.0, sale_date="2026-03-02")
])

# TASK 1: Create enriched sales report (10 min)
# Join sales with customers and products
# YOUR CODE HERE:




# TASK 2: Calculate metrics by industry and category (10 min)
# Total sales, average quantity, number of transactions
# YOUR CODE HERE:




# TASK 3: Write to Delta with partitioning (5 min)
# Partition by sale_date
# YOUR CODE HERE:




# TASK 4: Query optimization (5 min)
# Read back and filter by specific date
# YOUR CODE HERE:
```

**✅ Solution (reveal after attempt):**

```python
# SOLUTION:

# TASK 1: Enriched report
enriched_sales = sales \
    .join(customers, "customer_id", "inner") \
    .join(products, "product_id", "inner") \
    .select(
        "sale_id",
        "sale_date",
        customers.name.alias("customer_name"),
        "industry",
        products.name.alias("product_name"),
        "category",
        "quantity",
        "amount"
    )
enriched_sales.show()

# TASK 2: Metrics
metrics = enriched_sales.groupBy("industry", "category").agg(
    sum("amount").alias("total_sales"),
    avg("quantity").alias("avg_quantity"),
    count("*").alias("num_transactions")
).orderBy("total_sales", ascending=False)
metrics.show()

# TASK 3: Write to Delta
enriched_sales.write \
    .format("delta") \
    .mode("overwrite") \
    .partitionBy("sale_date") \
    .save("/tmp/delta/sales_enriched")

# TASK 4: Optimized query
sales_march1 = spark.read.format("delta") \
    .load("/tmp/delta/sales_enriched") \
    .filter("sale_date = '2026-03-01'")
print(f"March 1 sales: {sales_march1.count()}")
sales_march1.show()
```

---

## **Hour 4 (2:00-3:00): Python OOP for Data Engineering**

```python
# CREATE NOTEBOOK: "Day2_Python_OOP"

# CELL 1: Class basics for data pipelines
class DataPipeline:
    """Base class for ETL pipelines"""
    
    def __init__(self, name, source, destination):
        self.name = name
        self.source = source
        self.destination = destination
        self.status = "initialized"
    
    def run(self):
        """Execute pipeline"""
        print(f"Running pipeline: {self.name}")
        try:
            data = self.extract()
            clean_data = self.transform(data)
            self.load(clean_data)
            self.status = "completed"
        except Exception as e:
            self.status = "failed"
            raise e
    
    def extract(self):
        """Override in subclass"""
        raise NotImplementedError
    
    def transform(self, data):
        """Override in subclass"""
        return data
    
    def load(self, data):
        """Override in subclass"""
        pass

# CELL 2: Specific pipeline implementation
class SensorDataPipeline(DataPipeline):
    """Pipeline for sensor data migration"""
    
    def __init__(self, source_path, dest_path):
        super().__init__(
            name="Sensor Migration",
            source=source_path,
            destination=dest_path
        )
        self.spark = spark  # Databricks SparkSession
    
    def extract(self):
        """Read CSV from source"""
        print(f"Extracting from {self.source}")
        return self.spark.read.csv(self.source, header=True, inferSchema=True)
    
    def transform(self, data):
        """Clean and enrich data"""
        print("Transforming data...")
        from pyspark.sql.functions import col, when
        
        # Remove nulls
        clean = data.dropna()
        
        # Add quality flag
        enriched = clean.withColumn(
            "quality_flag",
            when(col("temperature") > 100, "ALERT")
            .when(col("temperature") > 90, "WARNING")
            .otherwise("NORMAL")
        )
        
        return enriched
    
    def load(self, data):
        """Write to Delta"""
        print(f"Loading to {self.destination}")
        data.write.format("delta").mode("overwrite").save(self.destination)

# CELL 3: Use the pipeline
# First, create sample data
sample_data = """train_id,temperature,vibration
TRAIN_001,85.5,2.3
TRAIN_001,95.2,3.1
TRAIN_002,105.1,5.8"""

dbutils.fs.put("/tmp/sensor_input.csv", sample_data, True)

# Run pipeline
pipeline = SensorDataPipeline(
    source_path="/tmp/sensor_input.csv",
    dest_path="/tmp/delta/sensor_clean"
)

pipeline.run()
print(f"Pipeline status: {pipeline.status}")

# Verify
result = spark.read.format("delta").load("/tmp/delta/sensor_clean")
result.show()
```

---

# 📅 DAY 3 (MARCH 5) - WINDOW FUNCTIONS + ERROR HANDLING

## **Hour 1 (9:00-10:00): PySpark Window Functions**

### **Read (20 min):**
- PySpark Window Functions docs
- Understand: PARTITION BY, ORDER BY, frame specifications

### **Watch (20 min):**
- "PySpark Window Functions Tutorial"

### **Concepts:**
- Running totals
- Moving averages
- Ranking
- Lag/Lead (previous/next values)

---

## **Hour 2 (10:00-11:00): Practice Windows**

```python
# CREATE NOTEBOOK: "Day3_Window_Functions"

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, lag, lead, sum, avg

# CELL 1: Create time-series data
time_series = spark.createDataFrame([
    Row(train_id="TRAIN_001", date="2026-03-01", fuel_used=500, distance=850),
    Row(train_id="TRAIN_001", date="2026-03-02", fuel_used=510, distance=820),
    Row(train_id="TRAIN_001", date="2026-03-03", fuel_used=495, distance=880),
    Row(train_id="TRAIN_002", date="2026-03-01", fuel_used=480, distance=900),
    Row(train_id="TRAIN_002", date="2026-03-02", fuel_used=490, distance=890),
    Row(train_id="TRAIN_002", date="2026-03-03", fuel_used=485, distance=910)
])

time_series.show()

# CELL 2: Window spec
window_by_train = Window.partitionBy("train_id").orderBy("date")

# CELL 3: Row number (sequential numbering)
df_with_row_num = time_series.withColumn(
    "day_number",
    row_number().over(window_by_train)
)
df_with_row_num.show()

# CELL 4: Running total (cumulative sum)
df_with_running_total = time_series.withColumn(
    "cumulative_fuel",
    sum("fuel_used").over(window_by_train)
)
df_with_running_total.show()

# CELL 5: Moving average (3-day window)
window_3days = Window.partitionBy("train_id").orderBy("date").rowsBetween(-2, 0)

df_with_ma = time_series.withColumn(
    "moving_avg_fuel",
    avg("fuel_used").over(window_3days)
)
df_with_ma.show()

# CELL 6: Previous day comparison (LAG)
df_with_prev = time_series.withColumn(
    "prev_day_fuel",
    lag("fuel_used", 1).over(window_by_train)
).withColumn(
    "fuel_change",
    col("fuel_used") - col("prev_day_fuel")
)
df_with_prev.show()

# CELL 7: Detect anomalies
df_anomaly = df_with_prev.withColumn(
    "anomaly_flag",
    when(abs(col("fuel_change")) > 20, "ANOMALY").otherwise("NORMAL")
)
df_anomaly.show()
```

---

## **Hour 3 (11:00-11:30): TIMED TASK (30 MIN)**

### **🏗️ MIGRATION SCENARIO: Time-Series Analysis**

**Scenario:** Analyzing sensor data trends to detect equipment failures (predictive maintenance)

```python
# CREATE NOTEBOOK: "Day3_Migration_Task"

# SETUP: Create sensor readings (5 min)
sensor_data = spark.createDataFrame([
    Row(sensor_id=1, timestamp="2026-03-01 10:00:00", temperature=85.0, pressure=120.0),
    Row(sensor_id=1, timestamp="2026-03-01 11:00:00", temperature=86.5, pressure=121.0),
    Row(sensor_id=1, timestamp="2026-03-01 12:00:00", temperature=92.0, pressure=125.0),  # Rising
    Row(sensor_id=1, timestamp="2026-03-01 13:00:00", temperature=98.5, pressure=130.0),  # Alert!
    Row(sensor_id=2, timestamp="2026-03-01 10:00:00", temperature=82.0, pressure=118.0),
    Row(sensor_id=2, timestamp="2026-03-01 11:00:00", temperature=83.0, pressure=119.0),
    Row(sensor_id=2, timestamp="2026-03-01 12:00:00", temperature=82.5, pressure=118.5),
    Row(sensor_id=2, timestamp="2026-03-01 13:00:00", temperature=83.5, pressure=119.5)
])

# TASK 1: Calculate hourly changes (10 min)
# Compare each reading with previous hour
# YOUR CODE HERE:




# TASK 2: 3-hour moving average (10 min)
# Smooth out noise in sensor data
# YOUR CODE HERE:




# TASK 3: Detect rapid temperature increases (5 min)
# Flag if temperature increases > 5 degrees in 1 hour
# YOUR CODE HERE:




# TASK 4: Write alert records to Delta (5 min)
# Only save records flagged as alerts
# YOUR CODE HERE:
```

---

## **Hour 4 (2:00-3:00): Python Error Handling**

```python
# CREATE NOTEBOOK: "Day3_Error_Handling"

# CELL 1: Try-Except basics
def process_sensor_reading(value):
    try:
        # Convert and validate
        temp = float(value)
        if temp < -50 or temp > 150:
            raise ValueError(f"Temperature {temp} out of range")
        return temp
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Test
print(process_sensor_reading("85.5"))  # Valid
print(process_sensor_reading("200"))    # Out of range
print(process_sensor_reading("abc"))    # Invalid

# CELL 2: Custom exceptions
class DataQualityError(Exception):
    """Raised when data quality checks fail"""
    pass

class DataValidationError(Exception):
    """Raised when data validation fails"""
    pass

def validate_dataframe(df, required_columns):
    """Validate DataFrame has required columns"""
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise DataValidationError(f"Missing columns: {missing}")
    
    # Check for nulls
    null_counts = df.select([
        sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
        for c in df.columns
    ]).collect()[0].asDict()
    
    null_cols = [c for c, count in null_counts.items() if count > 0]
    if null_cols:
        raise DataQualityError(f"Null values found in: {null_cols}")

# CELL 3: Production pipeline with error handling
class ProductionPipeline:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.errors = []
    
    def run(self):
        try:
            # Extract
            df = spark.read.csv(self.source, header=True, inferSchema=True)
            
            # Validate
            validate_dataframe(df, ["train_id", "temperature", "vibration"])
            
            # Transform
            clean_df = self.clean_data(df)
            
            # Load
            clean_df.write.format("delta").mode("overwrite").save(self.destination)
            
            return {"status": "success", "records": clean_df.count()}
            
        except DataValidationError as e:
            self.errors.append(str(e))
            return {"status": "failed", "error": str(e)}
        except DataQualityError as e:
            self.errors.append(str(e))
            return {"status": "failed", "error": str(e)}
        except Exception as e:
            self.errors.append(f"Unexpected error: {str(e)}")
            return {"status": "failed", "error": str(e)}
    
    def clean_data(self, df):
        # Remove duplicates, fill nulls, etc.
        return df.dropDuplicates().fillna(0)
```

---

# 📅 DAY 4 (MARCH 6) - DELTA LAKE + PERFORMANCE

## **Hour 1 (9:00-10:00): Delta Lake Fundamentals**

### **Read (30 min):**
- Databricks Delta Lake docs
- ACID transactions
- Time Travel
- Z-Ordering

### **Watch (30 min):**
- "Delta Lake Introduction" (Databricks YouTube)

---

## **Hour 2 (10:00-11:00): Delta Lake Operations**

```python
# CREATE NOTEBOOK: "Day4_Delta_Lake"

# CELL 1: Create Delta table
from delta.tables import DeltaTable

data = spark.createDataFrame([
    Row(id=1, name="Item A", quantity=100, price=50.0, date="2026-03-01"),
    Row(id=2, name="Item B", quantity=200, price=30.0, date="2026-03-01"),
    Row(id=3, name="Item C", quantity=150, price=40.0, date="2026-03-02")
])

# Write as Delta
data.write.format("delta").mode("overwrite").save("/tmp/delta/inventory")

# CELL 2: Read Delta
df_delta = spark.read.format("delta").load("/tmp/delta/inventory")
df_delta.show()

# CELL 3: Update records (ACID transaction)
deltaTable = DeltaTable.forPath(spark, "/tmp/delta/inventory")

deltaTable.update(
    condition="id = 1",
    set={"quantity": "150"}  # Update Item A quantity
)

# Verify
spark.read.format("delta").load("/tmp/delta/inventory").show()

# CELL 4: Delete records
deltaTable.delete("quantity < 50")
spark.read.format("delta").load("/tmp/delta/inventory").show()

# CELL 5: MERGE (Upsert) - CRITICAL for migrations!
updates = spark.createDataFrame([
    Row(id=2, name="Item B", quantity=250, price=32.0, date="2026-03-03"),  # Update
    Row(id=4, name="Item D", quantity=300, price=45.0, date="2026-03-03")   # Insert
])

deltaTable.alias("target").merge(
    updates.alias("source"),
    "target.id = source.id"
).whenMatchedUpdate(
    set={
        "quantity": "source.quantity",
        "price": "source.price",
        "date": "source.date"
    }
).whenNotMatchedInsert(
    values={
        "id": "source.id",
        "name": "source.name",
        "quantity": "source.quantity",
        "price": "source.price",
        "date": "source.date"
    }
).execute()

spark.read.format("delta").load("/tmp/delta/inventory").show()

# CELL 6: Time Travel (query old versions)
# Show version history
deltaTable.history().select("version", "timestamp", "operation").show()

# Query old version
df_v0 = spark.read.format("delta").option("versionAsOf", 0).load("/tmp/delta/inventory")
print("Version 0:")
df_v0.show()

# CELL 7: Optimize (compaction)
deltaTable.optimize().executeCompaction()

# CELL 8: Z-Order (multi-column optimization)
deltaTable.optimize().executeZOrderBy("date", "id")
```

---

## **Hour 3 (11:00-11:30): TIMED TASK (30 MIN)**

### **🏗️ MIGRATION SCENARIO: Incremental Load with CDC**

**Scenario:** Daily incremental updates from source system (Change Data Capture)

```python
# CREATE NOTEBOOK: "Day4_Migration_Task"

# SETUP: Initial load (5 min)
initial_data = spark.createDataFrame([
    Row(customer_id=1, name="Customer A", balance=1000.0, last_updated="2026-03-01"),
    Row(customer_id=2, name="Customer B", balance=2000.0, last_updated="2026-03-01"),
    Row(customer_id=3, name="Customer C", balance=1500.0, last_updated="2026-03-01")
])

initial_data.write.format("delta").mode("overwrite").save("/tmp/delta/customers")

# Day 2 changes (CDC from source)
changes_day2 = spark.createDataFrame([
    Row(customer_id=2, name="Customer B", balance=2500.0, last_updated="2026-03-02"),  # Update
    Row(customer_id=4, name="Customer D", balance=3000.0, last_updated="2026-03-02")   # Insert
])

# TASK 1: Implement MERGE for CDC (15 min)
# Update existing customers, insert new ones
# YOUR CODE HERE:




# TASK 2: Verify data quality (5 min)
# Check no duplicate customer_ids
# YOUR CODE HERE:




# TASK 3: Time Travel query (5 min)
# Show customers as of Day 1
# YOUR CODE HERE:




# TASK 4: Optimize table (5 min)
# Compact small files and Z-Order by customer_id
# YOUR CODE HERE:
```

---

## **Hour 4 (2:00-3:00): Performance Optimization**

```python
# CREATE NOTEBOOK: "Day4_Performance"

# CELL 1: Check partitions
df = spark.read.format("delta").load("/tmp/delta/customers")
print(f"Current partitions: {df.rdd.getNumPartitions()}")

# CELL 2: Repartition (increase parallelism)
df_repartitioned = df.repartition(10)
print(f"After repartition: {df_repartitioned.rdd.getNumPartitions()}")

# CELL 3: Coalesce (reduce partitions, no shuffle)
df_coalesced = df_repartitioned.coalesce(5)
print(f"After coalesce: {df_coalesced.rdd.getNumPartitions()}")

# CELL 4: Partition by column (for writes)
df.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("last_updated") \
    .save("/tmp/delta/customers_partitioned")

# Check partitions created
display(dbutils.fs.ls("/tmp/delta/customers_partitioned"))

# CELL 5: Caching (for reused DataFrames)
df_cached = df.cache()
df_cached.count()  # Materialize cache

# Subsequent operations faster
df_cached.filter("balance > 1500").count()
df_cached.groupBy("last_updated").count().show()

# Clear cache when done
df_cached.unpersist()

# CELL 6: Explain plan (understand query execution)
df.filter("balance > 1500").explain(extended=True)

# CELL 7: Broadcast join (small table optimization)
from pyspark.sql.functions import broadcast

large_table = spark.read.format("delta").load("/tmp/delta/sales_enriched")
small_table = spark.read.format("delta").load("/tmp/delta/customers")

# Broadcast small table to all workers
optimized_join = large_table.join(broadcast(small_table), "customer_id")
```

---

# 📅 DAY 5 (MARCH 7) - END-TO-END MIGRATION PROJECT

## **Hour 1-4 (9:00-1:00): FULL MIGRATION PROJECT (4 HOURS)**

### **🏗️ CAPSTONE: Legacy Oracle to Databricks Migration**

**Scenario:** Complete end-to-end migration like your 400TB project

```python
# CREATE NOTEBOOK: "Day5_Full_Migration_Project"

# ============================================
# PROJECT: E-COMMERCE DATA WAREHOUSE MIGRATION
# Source: Legacy Oracle (simulated with CSV)
# Target: Databricks Delta Lake
# Architecture: Medallion (Bronze → Silver → Gold)
# ============================================

# PART 1: BRONZE LAYER - Raw Ingestion (30 min)

# CELL 1: Create source data (simulating Oracle export)
# Customer dimension
customers_csv = """customer_id,name,email,city,country,signup_date
1,Alice Johnson,alice@email.com,New York,USA,2025-01-15
2,Bob Smith,bob@email.com,London,UK,2025-02-20
3,Charlie Brown,charlie@email.com,Toronto,Canada,2025-01-10
4,Diana Prince,diana@email.com,Sydney,Australia,2025-03-01"""

# Product dimension
products_csv = """product_id,name,category,price,supplier_id
101,Laptop Pro,Electronics,1200.00,1
102,Wireless Mouse,Electronics,25.00,1
103,Office Chair,Furniture,350.00,2
104,Standing Desk,Furniture,800.00,2
105,Notebook Set,Stationery,15.00,3"""

# Orders fact
orders_csv = """order_id,customer_id,product_id,quantity,order_date,status
1001,1,101,1,2026-03-01,completed
1002,1,102,2,2026-03-01,completed
1003,2,103,1,2026-03-02,completed
1004,3,101,1,2026-03-02,pending
1005,2,105,5,2026-03-03,completed
1006,4,104,1,2026-03-03,completed"""

# Write to DBFS
dbutils.fs.put("/tmp/source/customers.csv", customers_csv, True)
dbutils.fs.put("/tmp/source/products.csv", products_csv, True)
dbutils.fs.put("/tmp/source/orders.csv", orders_csv, True)

# CELL 2: Bronze ingestion (append-only, immutable)
from pyspark.sql.functions import current_timestamp, input_file_name

# Read customers
bronze_customers = spark.read.csv("/tmp/source/customers.csv", header=True, inferSchema=True) \
    .withColumn("ingestion_time", current_timestamp()) \
    .withColumn("source_file", input_file_name())

# Write to Bronze
bronze_customers.write.format("delta").mode("overwrite").save("/tmp/delta/bronze/customers")

# Repeat for products and orders
bronze_products = spark.read.csv("/tmp/source/products.csv", header=True, inferSchema=True) \
    .withColumn("ingestion_time", current_timestamp()) \
    .withColumn("source_file", input_file_name())
bronze_products.write.format("delta").mode("overwrite").save("/tmp/delta/bronze/products")

bronze_orders = spark.read.csv("/tmp/source/orders.csv", header=True, inferSchema=True) \
    .withColumn("ingestion_time", current_timestamp()) \
    .withColumn("source_file", input_file_name())
bronze_orders.write.format("delta").mode("overwrite").save("/tmp/delta/bronze/orders")

print("✅ Bronze layer completed")

# ============================================
# PART 2: SILVER LAYER - Cleaned & Validated (45 min)

# CELL 3: Silver - Data quality checks
from pyspark.sql.functions import col, trim, upper, to_date

# Read from Bronze
bronze_cust = spark.read.format("delta").load("/tmp/delta/bronze/customers")

# Clean customers
silver_customers = bronze_cust \
    .dropDuplicates(["customer_id"]) \
    .withColumn("email", trim(col("email"))) \
    .withColumn("country", upper(col("country"))) \
    .withColumn("signup_date", to_date(col("signup_date"))) \
    .filter(col("email").isNotNull())  # Data quality: email required

# Write to Silver
silver_customers.write.format("delta").mode("overwrite").save("/tmp/delta/silver/customers")

# CELL 4: Silver - Products with validation
bronze_prod = spark.read.format("delta").load("/tmp/delta/bronze/products")

silver_products = bronze_prod \
    .dropDuplicates(["product_id"]) \
    .filter(col("price") > 0)  # Validate price > 0

silver_products.write.format("delta").mode("overwrite").save("/tmp/delta/silver/products")

# CELL 5: Silver - Orders with enrichment
bronze_ord = spark.read.format("delta").load("/tmp/delta/bronze/orders")

silver_orders = bronze_ord \
    .withColumn("order_date", to_date(col("order_date"))) \
    .filter(col("quantity") > 0)  # Validate quantity

# Add calculated fields
silver_orders = silver_orders.join(
    silver_products.select("product_id", "price"),
    "product_id"
).withColumn("order_total", col("quantity") * col("price"))

silver_orders.write.format("delta").mode("overwrite").save("/tmp/delta/silver/orders")

print("✅ Silver layer completed")

# ============================================
# PART 3: GOLD LAYER - Business Aggregates (45 min)

# CELL 6: Gold - Customer metrics
silver_cust = spark.read.format("delta").load("/tmp/delta/silver/customers")
silver_ord = spark.read.format("delta").load("/tmp/delta/silver/orders")

customer_metrics = silver_ord.groupBy("customer_id").agg(
    sum("order_total").alias("lifetime_value"),
    count("order_id").alias("total_orders"),
    avg("order_total").alias("avg_order_value")
).join(silver_cust, "customer_id")

customer_metrics.write.format("delta").mode("overwrite") \
    .save("/tmp/delta/gold/customer_metrics")

# CELL 7: Gold - Product performance
product_performance = silver_ord.groupBy("product_id").agg(
    sum("quantity").alias("total_units_sold"),
    sum("order_total").alias("total_revenue"),
    count("order_id").alias("num_orders")
).join(silver_products, "product_id")

product_performance.write.format("delta").mode("overwrite") \
    .save("/tmp/delta/gold/product_performance")

# CELL 8: Gold - Daily sales summary
daily_sales = silver_ord.groupBy("order_date").agg(
    sum("order_total").alias("daily_revenue"),
    count("order_id").alias("num_orders"),
    countDistinct("customer_id").alias("unique_customers")
)

daily_sales.write.format("delta").mode("overwrite") \
    .partitionBy("order_date") \
    .save("/tmp/delta/gold/daily_sales")

print("✅ Gold layer completed")

# ============================================
# PART 4: OPTIMIZATION & VALIDATION (60 min)

# CELL 9: Optimize tables
from delta.tables import DeltaTable

# Optimize all Silver tables
for table in ["customers", "products", "orders"]:
    deltaTable = DeltaTable.forPath(spark, f"/tmp/delta/silver/{table}")
    deltaTable.optimize().executeCompaction()
    print(f"✅ Optimized silver.{table}")

# Z-Order important columns
orders_table = DeltaTable.forPath(spark, "/tmp/delta/silver/orders")
orders_table.optimize().executeZOrderBy("order_date", "customer_id")

# CELL 10: Data validation
# Check record counts
bronze_count = spark.read.format("delta").load("/tmp/delta/bronze/orders").count()
silver_count = spark.read.format("delta").load("/tmp/delta/silver/orders").count()
print(f"Bronze orders: {bronze_count}")
print(f"Silver orders: {silver_count}")
print(f"Quality filter removed: {bronze_count - silver_count} records")

# CELL 11: Query performance test
# Before optimization
import time

start = time.time()
result = spark.read.format("delta").load("/tmp/delta/silver/orders") \
    .filter("order_date = '2026-03-02'").count()
elapsed = time.time() - start
print(f"Query took {elapsed:.2f}s, returned {result} records")

# CELL 12: Final report
print("\n" + "="*50)
print("MIGRATION PROJECT SUMMARY")
print("="*50)

print("\nBronze Layer (Raw):")
print(f"  - Customers: {spark.read.format('delta').load('/tmp/delta/bronze/customers').count()}")
print(f"  - Products: {spark.read.format('delta').load('/tmp/delta/bronze/products').count()}")
print(f"  - Orders: {spark.read.format('delta').load('/tmp/delta/bronze/orders').count()}")

print("\nSilver Layer (Cleaned):")
print(f"  - Customers: {spark.read.format('delta').load('/tmp/delta/silver/customers').count()}")
print(f"  - Products: {spark.read.format('delta').load('/tmp/delta/silver/products').count()}")
print(f"  - Orders: {spark.read.format('delta').load('/tmp/delta/silver/orders').count()}")

print("\nGold Layer (Aggregates):")
print(f"  - Customer Metrics: {spark.read.format('delta').load('/tmp/delta/gold/customer_metrics').count()}")
print(f"  - Product Performance: {spark.read.format('delta').load('/tmp/delta/gold/product_performance').count()}")
print(f"  - Daily Sales: {spark.read.format('delta').load('/tmp/delta/gold/daily_sales').count()}")

print("\n✅ MIGRATION COMPLETED SUCCESSFULLY!")
```

---

## 📊 5-DAY SUMMARY

**What You've Learned:**

### **PySpark (Beginner → Intermediate):**
- ✅ DataFrame API (select, filter, groupBy)
- ✅ Joins (inner, left, broadcast)
- ✅ Aggregations & window functions
- ✅ Delta Lake operations (ACID, merge, time travel)
- ✅ Performance optimization (partitioning, caching, Z-order)

### **Python (Intermediate → Advanced):**
- ✅ OOP (classes, inheritance, polymorphism)
- ✅ Error handling (try/except, custom exceptions)
- ✅ Functional programming (lambda, map, filter)
- ✅ List comprehensions
- ✅ Production code patterns

### **Databricks (Beginner → Intermediate):**
- ✅ Cluster management
- ✅ Notebook workflows
- ✅ Delta Lake (Medallion Architecture)
- ✅ DBFS file system
- ✅ Optimization techniques

### **Real Migration Skills:**
- ✅ Bronze/Silver/Gold pattern
- ✅ Data quality checks
- ✅ Incremental loads (CDC)
- ✅ Performance tuning
- ✅ End-to-end pipeline

---

## 🎯 INTERVIEW READY TALKING POINTS

**After 5 days, you can say:**

**"I've built production Medallion Architecture pipelines in Databricks, implementing Bronze for raw ingestion, Silver for validated data with quality checks, and Gold for business-ready aggregates. I've optimized Delta tables using Z-Ordering and compaction, and implemented incremental loads using MERGE for change data capture."**

**"I use PySpark window functions for time-series analysis, detecting anomalies in sensor data by comparing running averages with threshold values. I've optimized joins using broadcast for small dimension tables and partitioned fact tables by date for query performance."**

**"In my migration projects, I implement comprehensive error handling with custom exceptions for data quality issues, using try-except blocks to ensure pipeline resilience. I follow OOP principles, building reusable pipeline classes with inheritance for different data sources."**

---

## ✅ FINAL CHECKLIST

**By Day 5 end, you should have:**
- [ ] 15+ Databricks notebooks created
- [ ] 5 timed migration tasks completed
- [ ] Full Medallion Architecture implemented
- [ ] Performance optimization practiced
- [ ] Error handling patterns learned
- [ ] OOP pipelines built
- [ ] Window functions mastered
- [ ] Delta Lake operations fluent

**You're now ready for Insight, BNSF, and Cognizant technical interviews!** 🔥

---

**START DAY 1 TOMORROW MORNING (MARCH 3, 9:00 AM)** ⏰

**YOU'VE GOT THIS!** 💪🚀
