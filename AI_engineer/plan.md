# 🎯 FOCUSED 10-DAY PLAN - PySpark (2→9) + Python (6→9) + AI Pipelines

## 📊 YOUR CURRENT STATE & GOALS

**Current Skills:**
- Python: 6/10 (good foundation, need advanced topics)
- PySpark: 2/10 (basics only, need deep dive)
- SQL: Strong (no focus needed) ✅

**Target Skills (Day 10):**
- Python: 9/10 (production-grade, design patterns, advanced)
- PySpark: 9/10 (expert transformations, optimization, architecture)
- AI Pipelines: 7/10 (sklearn, model serving, MLOps basics)

**Time:** 10 days, 4 hours/day = 40 hours total

---

## 🎯 TIME ALLOCATION STRATEGY

### **Daily 4-Hour Breakdown:**

**2 hours: PySpark Deep Dive** (50%) ⭐⭐⭐⭐⭐
- Most critical gap (2→9 is huge leap)
- Needed for Cognizant Round 2-3
- Overlaps with BNSF data engineering

**1.5 hours: Advanced Python** (37.5%) ⭐⭐⭐⭐
- Already at 6/10, push to 9/10
- OOP, design patterns, production practices
- Needed for BNSF AI Engineer

**0.5 hour: AI Pipelines Integration** (12.5%) ⭐⭐⭐
- Tie PySpark + Python together
- sklearn in PySpark context
- Model deployment patterns

---

## 🚀 10-DAY ACCELERATED PLAN

---

# **DAY 1 (FEB 26)** - PySpark Foundations + Python OOP

### **Morning: 9:00-11:00 (2 hrs) - PySpark Fundamentals**

**9:00-9:45 (45 min): Setup & Basics**
- [ ] Install PySpark locally: `pip install pyspark --break-system-packages`
- [ ] Databricks Community Edition login (community.cloud.databricks.com)
- [ ] Read: PySpark Quick Start (pyspark.apache.org)
- [ ] Understand: RDD vs DataFrame vs Dataset

**9:45-11:00 (75 min): DataFrame API Deep Dive**

**Core transformations (practice each):**
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create session
spark = SparkSession.builder \
    .appName("Learning") \
    .master("local[*]") \
    .getOrCreate()

# Read data (CSV, JSON, Parquet, Delta)
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("/path/to/data.csv")

# SELECTION & FILTERING
df.select("col1", "col2")
df.select(col("amount") * 1.1)  # With transformation
df.filter(col("amount") > 1000)
df.where((col("status") == "active") & (col("amount") > 1000))

# COLUMN OPERATIONS
df.withColumn("new_col", col("amount") * 2)
df.withColumnRenamed("old_name", "new_name")
df.drop("unwanted_col")

# AGGREGATIONS
df.groupBy("category").agg(
    sum("amount").alias("total_amount"),
    avg("amount").alias("avg_amount"),
    count("*").alias("count"),
    max("date").alias("latest_date")
)

# SORTING
df.orderBy("date", ascending=False)
df.sort(col("amount").desc())

# Show results
df.show(10)
df.printSchema()
print(f"Count: {df.count()}")
```

**Practice Exercise:**
- [ ] Load sample dataset (use Databricks sample data)
- [ ] Perform 10 different transformations
- [ ] Write results to Delta format

---

### **Afternoon: 11:00-12:30 (1.5 hrs) - Advanced Python OOP**

**11:00-11:45 (45 min): Classes, Inheritance, Polymorphism**

```python
# Base class with proper OOP principles
class DataPipeline:
    """Base class for all data pipelines"""
    
    def __init__(self, name, source, destination):
        self.name = name
        self.source = source
        self.destination = destination
        self._status = "initialized"
    
    def extract(self):
        """Extract data from source - to be overridden"""
        raise NotImplementedError("Subclass must implement extract()")
    
    def transform(self, data):
        """Transform data - to be overridden"""
        raise NotImplementedError("Subclass must implement transform()")
    
    def load(self, data):
        """Load data to destination"""
        print(f"Loading data to {self.destination}")
    
    def run(self):
        """Execute full pipeline"""
        print(f"Running pipeline: {self.name}")
        data = self.extract()
        transformed = self.transform(data)
        self.load(transformed)
        self._status = "completed"
    
    @property
    def status(self):
        """Property decorator for status"""
        return self._status
    
    def __repr__(self):
        return f"DataPipeline(name={self.name}, status={self.status})"

# Inheritance - Specific pipeline types
class BatchPipeline(DataPipeline):
    """Batch processing pipeline"""
    
    def extract(self):
        print(f"Batch extracting from {self.source}")
        return {"data": "batch_data"}
    
    def transform(self, data):
        print("Applying batch transformations")
        return data

class StreamingPipeline(DataPipeline):
    """Real-time streaming pipeline"""
    
    def __init__(self, name, source, destination, window_size):
        super().__init__(name, source, destination)
        self.window_size = window_size
    
    def extract(self):
        print(f"Streaming from {self.source} with window {self.window_size}")
        return {"data": "streaming_data"}
    
    def transform(self, data):
        print("Applying streaming transformations")
        return data

# Polymorphism - same interface, different behavior
def execute_pipeline(pipeline: DataPipeline):
    """Execute any pipeline type"""
    pipeline.run()
    print(f"Pipeline status: {pipeline.status}")

# Usage
batch = BatchPipeline("daily_load", "s3://bucket", "delta_table")
streaming = StreamingPipeline("realtime", "kafka://topic", "delta_table", "5min")

execute_pipeline(batch)
execute_pipeline(streaming)
```

**11:45-12:30 (45 min): Design Patterns**

```python
# SINGLETON PATTERN - Database connection manager
class DatabaseManager:
    """Singleton for DB connections"""
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def connect(self):
        if self._connection is None:
            print("Creating new connection")
            self._connection = "DB_CONNECTION_OBJECT"
        return self._connection
    
    def disconnect(self):
        if self._connection:
            print("Closing connection")
            self._connection = None

# Usage - always returns same instance
db1 = DatabaseManager()
db2 = DatabaseManager()
print(db1 is db2)  # True - same object

# FACTORY PATTERN - Create different connectors
class DataConnector:
    def connect(self):
        pass

class S3Connector(DataConnector):
    def connect(self):
        return "S3 Connection"

class KafkaConnector(DataConnector):
    def connect(self):
        return "Kafka Connection"

class SnowflakeConnector(DataConnector):
    def connect(self):
        return "Snowflake Connection"

class ConnectorFactory:
    """Factory to create appropriate connector"""
    
    @staticmethod
    def create(connector_type):
        connectors = {
            "s3": S3Connector,
            "kafka": KafkaConnector,
            "snowflake": SnowflakeConnector
        }
        connector_class = connectors.get(connector_type)
        if connector_class:
            return connector_class()
        raise ValueError(f"Unknown connector: {connector_type}")

# Usage
s3_conn = ConnectorFactory.create("s3")
kafka_conn = ConnectorFactory.create("kafka")

# STRATEGY PATTERN - Different transformation strategies
class TransformationStrategy:
    def transform(self, data):
        pass

class CleaningStrategy(TransformationStrategy):
    def transform(self, data):
        print("Cleaning: removing nulls, duplicates")
        return data

class EnrichmentStrategy(TransformationStrategy):
    def transform(self, data):
        print("Enrichment: adding calculated fields")
        return data

class AggregationStrategy(TransformationStrategy):
    def transform(self, data):
        print("Aggregation: grouping and summing")
        return data

class DataProcessor:
    """Context that uses strategy"""
    def __init__(self, strategy: TransformationStrategy):
        self.strategy = strategy
    
    def process(self, data):
        return self.strategy.transform(data)

# Usage - swap strategies at runtime
processor = DataProcessor(CleaningStrategy())
processor.process(data)

processor.strategy = EnrichmentStrategy()
processor.process(data)
```

**Practice:**
- [ ] Implement these patterns in your own examples
- [ ] LeetCode: "Design HashMap", "Design Parking System"

---

### **Evening: 7:00-7:30 (30 min) - AI Pipeline Basics**

**Concept: End-to-End ML Pipeline**

```python
# Conceptual AI Pipeline Architecture
class MLPipeline:
    """
    End-to-end ML pipeline
    
    Stages:
    1. Data Extraction (PySpark)
    2. Feature Engineering (PySpark)
    3. Model Training (sklearn/TensorFlow)
    4. Model Evaluation
    5. Model Deployment (API)
    6. Monitoring
    """
    
    def __init__(self):
        self.spark = None
        self.model = None
    
    def extract_features(self):
        """Use PySpark to extract features from big data"""
        pass
    
    def train_model(self, features):
        """Train sklearn model on prepared features"""
        pass
    
    def deploy_model(self):
        """Deploy as REST API"""
        pass
```

- [ ] Read: "What is MLOps?" (5 min)
- [ ] Watch: "ML Pipeline Overview" YouTube (10 min)
- [ ] Sketch: Your understanding of ML pipeline stages

---

# **DAY 2 (FEB 27)** - PySpark Joins + Python Advanced Features

### **Morning: 9:00-11:00 (2 hrs) - PySpark Joins & Window Functions**

**9:00-10:00 (1 hr): Joins Mastery**

```python
from pyspark.sql.functions import broadcast

# Sample data
customers = spark.createDataFrame([
    (1, "Alice", "NY"),
    (2, "Bob", "CA"),
    (3, "Charlie", "TX")
], ["id", "name", "state"])

orders = spark.createDataFrame([
    (101, 1, 150.0, "2026-01-15"),
    (102, 1, 200.0, "2026-02-20"),
    (103, 2, 100.0, "2026-01-10"),
    (104, 4, 50.0, "2026-02-15")  # No matching customer
], ["order_id", "customer_id", "amount", "date"])

# INNER JOIN (only matching records)
inner_result = customers.join(
    orders,
    customers.id == orders.customer_id,
    "inner"
)

# LEFT JOIN (all customers, even without orders)
left_result = customers.join(
    orders,
    customers.id == orders.customer_id,
    "left"
)

# RIGHT JOIN (all orders, even without matching customer)
right_result = customers.join(
    orders,
    customers.id == orders.customer_id,
    "right"
)

# FULL OUTER JOIN (all records from both)
full_result = customers.join(
    orders,
    customers.id == orders.customer_id,
    "full"
)

# BROADCAST JOIN (optimize for small tables)
# Use when one table is small (< 10MB)
small_dim = customers  # Dimension table
large_fact = orders    # Fact table

optimized_join = large_fact.join(
    broadcast(small_dim),
    large_fact.customer_id == small_dim.id
)

# SELF JOIN (compare rows within same table)
df.alias("df1").join(
    df.alias("df2"),
    col("df1.manager_id") == col("df2.employee_id")
)

# CROSS JOIN (Cartesian product - use cautiously!)
customers.crossJoin(orders)  # Every customer with every order
```

**10:00-11:00 (1 hr): Window Functions**

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, lag, lead

# Sample transaction data
transactions = spark.createDataFrame([
    ("2026-01-01", "Alice", 100),
    ("2026-01-02", "Alice", 150),
    ("2026-01-03", "Alice", 120),
    ("2026-01-01", "Bob", 200),
    ("2026-01-02", "Bob", 180),
], ["date", "customer", "amount"])

# WINDOW SPEC - define partitioning and ordering
customer_window = Window.partitionBy("customer").orderBy("date")

# ROW_NUMBER - sequential numbering within partition
df_with_row_num = transactions.withColumn(
    "row_num",
    row_number().over(customer_window)
)

# RANK - with gaps for ties
df_with_rank = transactions.withColumn(
    "rank",
    rank().over(Window.partitionBy("customer").orderBy(col("amount").desc()))
)

# RUNNING TOTAL (cumulative sum)
df_with_running_total = transactions.withColumn(
    "running_total",
    sum("amount").over(customer_window)
)

# MOVING AVERAGE (rolling average)
window_3_rows = Window.partitionBy("customer").orderBy("date").rowsBetween(-2, 0)
df_with_moving_avg = transactions.withColumn(
    "moving_avg_3",
    avg("amount").over(window_3_rows)
)

# LAG - previous row value
df_with_previous = transactions.withColumn(
    "previous_amount",
    lag("amount", 1).over(customer_window)
)

# LEAD - next row value
df_with_next = transactions.withColumn(
    "next_amount",
    lead("amount", 1).over(customer_window)
)

# COMPARE WITH PREVIOUS
df_with_change = transactions.withColumn(
    "previous_amount",
    lag("amount").over(customer_window)
).withColumn(
    "amount_change",
    col("amount") - col("previous_amount")
)

# PERCENTILE within group
df_with_percentile = transactions.withColumn(
    "percentile",
    percent_rank().over(Window.partitionBy("customer").orderBy("amount"))
)

df_with_change.show()
```

**Practice:**
- [ ] M&T Bank scenario: Calculate running balance per customer
- [ ] Identify top 3 transactions per customer (rank)
- [ ] Calculate 7-day moving average

---

### **Afternoon: 11:00-12:30 (1.5 hrs) - Python: Decorators & Generators**

**11:00-12:00 (1 hr): Decorators**

```python
import time
import functools
from typing import Callable

# BASIC DECORATOR - timing
def timer(func: Callable) -> Callable:
    """Measure execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# DECORATOR WITH ARGUMENTS
def retry(max_attempts: int = 3, delay: float = 1):
    """Retry function on failure"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def flaky_api_call():
    # Might fail
    import random
    if random.random() < 0.7:
        raise Exception("API Error")
    return "Success"

# LOGGING DECORATOR
def log_calls(func):
    """Log function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

# VALIDATION DECORATOR
def validate_positive(func):
    """Ensure all numeric arguments are positive"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument must be positive: {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_price(quantity, unit_price):
    return quantity * unit_price

# STACKING DECORATORS
@timer
@retry(max_attempts=3)
@log_calls
def complex_function(x):
    return x * 2
```

**12:00-12:30 (30 min): Generators**

```python
# BASIC GENERATOR - memory efficient
def count_up_to(n):
    """Generator that counts from 1 to n"""
    i = 1
    while i <= n:
        yield i
        i += 1

# Usage - doesn't create list in memory
for num in count_up_to(1000000):
    if num > 10:
        break
    print(num)

# GENERATOR FOR FILE PROCESSING (critical for big data)
def process_large_file(filename):
    """Process file line by line - memory efficient"""
    with open(filename, 'r') as f:
        for line in f:
            # Process line
            cleaned = line.strip()
            if cleaned:
                yield cleaned

# GENERATOR PIPELINE
def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def transform_lines(lines):
    for line in lines:
        yield line.upper()

# Compose generators
lines = read_file("data.txt")
filtered = filter_lines(lines, "error")
transformed = transform_lines(filtered)

for line in transformed:
    print(line)

# GENERATOR EXPRESSION (like list comprehension)
# List comprehension - creates full list in memory
squares_list = [x**2 for x in range(1000000)]  # Memory intensive

# Generator expression - lazy evaluation
squares_gen = (x**2 for x in range(1000000))  # Memory efficient

# FIBONACCI GENERATOR
def fibonacci():
    """Infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use with itertools
from itertools import islice
first_10_fibs = list(islice(fibonacci(), 10))

# DATA PIPELINE WITH GENERATORS (BNSF-style)
def extract_data():
    """Extract from source"""
    for i in range(100):
        yield {"id": i, "value": i * 10}

def transform_data(records):
    """Transform records"""
    for record in records:
        record["value"] = record["value"] * 1.1
        yield record

def load_data(records):
    """Load to destination"""
    for record in records:
        # Save to database
        print(f"Saving: {record}")

# Execute pipeline - memory efficient!
pipeline = load_data(transform_data(extract_data()))
# Nothing happens until we iterate
for _ in pipeline:
    pass  # Just consume the generator
```

---

### **Evening: 7:00-7:30 (30 min) - Connect PySpark + Python**

```python
# Use Python generators in PySpark UDFs
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

@udf(returnType=StringType())
def clean_text_udf(text):
    """Python function used in PySpark"""
    if text:
        return text.strip().upper()
    return ""

df_cleaned = df.withColumn("cleaned_name", clean_text_udf(col("name")))
```

- [ ] Think: How can decorators help in PySpark pipelines?
- [ ] Sketch: ML pipeline using generators for data loading

---

# **DAY 3 (FEB 28)** - PySpark Optimization + Python Context Managers

### **Morning: 9:00-11:00 (2 hrs) - PySpark Performance Optimization**

**9:00-10:00 (1 hr): Partitioning & Shuffling**

```python
from pyspark.sql.functions import spark_partition_id

# CHECK CURRENT PARTITIONS
print(f"Number of partitions: {df.rdd.getNumPartitions()}")

# See data distribution across partitions
df.withColumn("partition_id", spark_partition_id()).show()

# REPARTITION - increase partitions (shuffle!)
df_more_partitions = df.repartition(100)

# Repartition by column (for better locality)
df_by_date = df.repartition(50, "date")

# COALESCE - reduce partitions (no shuffle)
df_fewer_partitions = df.coalesce(10)

# WHY PARTITIONING MATTERS:
# - Too few partitions: underutilized cluster
# - Too many partitions: high overhead
# - Rule of thumb: 2-4 partitions per CPU core

# PARTITION BY COLUMN (for Parquet/Delta writes)
df.write \
    .partitionBy("year", "month") \
    .format("parquet") \
    .save("/path/to/data")

# Reading partitioned data (partition pruning)
df_filtered = spark.read.parquet("/path/to/data") \
    .filter(col("year") == 2026)  # Only reads 2026 partitions!

# BUCKETING - for repeated joins
df.write \
    .bucketBy(100, "customer_id") \
    .sortBy("date") \
    .saveAsTable("bucketed_transactions")

# AVOID SHUFFLE when possible
# Bad - causes shuffle
df.groupBy("customer_id").count()  # Shuffle to group data

# Better - if already partitioned by customer_id
df_partitioned = df.repartition("customer_id")
df_partitioned.groupBy("customer_id").count()  # Less shuffle

# BROADCAST JOIN - avoid shuffle for small tables
from pyspark.sql.functions import broadcast

large_df = spark.read.parquet("/large_dataset")
small_df = spark.read.parquet("/small_lookup")  # < 10MB

# Bad - shuffle both tables
result = large_df.join(small_df, "key")

# Good - broadcast small table to all nodes
result = large_df.join(broadcast(small_df), "key")
```

**10:00-11:00 (1 hr): Caching & Persistence**

```python
from pyspark import StorageLevel

# CACHE - store in memory (default)
df_cached = df.cache()
df_cached.count()  # Trigger action to materialize cache

# Subsequent actions are fast
df_cached.show()  # No re-computation
df_cached.filter(col("amount") > 100).count()  # Uses cache

# UNPERSIST - free memory
df_cached.unpersist()

# PERSIST with different storage levels
df.persist(StorageLevel.MEMORY_ONLY)  # In memory, lose if evicted
df.persist(StorageLevel.MEMORY_AND_DISK)  # Spill to disk if needed
df.persist(StorageLevel.DISK_ONLY)  # Store on disk
df.persist(StorageLevel.MEMORY_ONLY_SER)  # Serialized (save memory)

# WHEN TO CACHE:
# 1. Iterative algorithms (ML training)
# 2. Reused DataFrames in same query
# 3. Interactive analysis

# WHEN NOT TO CACHE:
# 1. One-time use
# 2. Data larger than available memory
# 3. Cheap to recompute

# CHECKPOINT - write to reliable storage
df.write.parquet("/tmp/checkpoint")
df_checkpointed = spark.read.parquet("/tmp/checkpoint")

# ADAPTIVE QUERY EXECUTION (AQE) - Spark 3.0+
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

# AQE automatically:
# - Coalesces small partitions
# - Optimizes skew joins
# - Converts sort-merge to broadcast join

# EXPLAIN PLAN - understand query execution
df.explain()  # Physical plan
df.explain(extended=True)  # Detailed plan

# MONITOR PERFORMANCE
# Use Spark UI: http://localhost:4040
# Check: DAG, stages, tasks, shuffles, caching
```

**Practice Exercise:**
- [ ] Load large dataset (use Databricks sample data)
- [ ] Optimize joins with broadcast
- [ ] Cache intermediate results
- [ ] Compare execution times (explain plan)

---

### **Afternoon: 11:00-12:30 (1.5 hrs) - Python: Context Managers & Advanced Features**

**11:00-12:00 (1 hr): Context Managers**

```python
# BASIC CONTEXT MANAGER - file handling
with open("file.txt", "r") as f:
    data = f.read()
# File automatically closed

# CUSTOM CONTEXT MANAGER - using class
class DatabaseConnection:
    """Context manager for DB connections"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Connecting to {self.connection_string}")
        self.connection = "DB_CONNECTION"  # Actual connection
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        print("Closing connection")
        if self.connection:
            self.connection = None
        
        # Handle exceptions
        if exc_type:
            print(f"Exception occurred: {exc_val}")
            return False  # Re-raise exception
        return True

# Usage
with DatabaseConnection("postgresql://localhost") as conn:
    # Use connection
    print(f"Using: {conn}")
    # Connection automatically closed

# CONTEXT MANAGER USING @contextmanager
from contextlib import contextmanager

@contextmanager
def timer_context(name):
    """Time a code block"""
    print(f"Starting {name}")
    start = time.time()
    try:
        yield  # Code block executes here
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.4f}s")

# Usage
with timer_context("Data Processing"):
    # Your code
    time.sleep(1)

# NESTED CONTEXT MANAGERS
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())

# CUSTOM: SPARK SESSION MANAGER
@contextmanager
def spark_session(app_name):
    """Manage Spark session lifecycle"""
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    try:
        yield spark
    finally:
        spark.stop()

# Usage
with spark_session("MyApp") as spark:
    df = spark.read.csv("data.csv")
    df.show()
# Spark automatically stopped

# TRANSACTION CONTEXT MANAGER
@contextmanager
def database_transaction(conn):
    """Handle DB transactions"""
    try:
        yield conn
        conn.commit()
        print("Transaction committed")
    except Exception as e:
        conn.rollback()
        print(f"Transaction rolled back: {e}")
        raise

# SUPPRESSING EXCEPTIONS
from contextlib import suppress

# Instead of try/except
with suppress(FileNotFoundError):
    os.remove("nonexistent_file.txt")
# No error raised
```

**12:00-12:30 (30 min): Type Hints & Dataclasses**

```python
from typing import List, Dict, Optional, Union, Tuple
from dataclasses import dataclass, field
from datetime import datetime

# TYPE HINTS - improve code quality
def process_data(
    records: List[Dict[str, Union[str, int]]],
    threshold: float = 0.5
) -> Tuple[List[Dict], int]:
    """
    Process records and return filtered results
    
    Args:
        records: List of dictionaries with mixed types
        threshold: Filter threshold
    
    Returns:
        Tuple of (filtered_records, count)
    """
    filtered = [r for r in records if r.get("value", 0) > threshold]
    return filtered, len(filtered)

# DATACLASSES - clean data structures
@dataclass
class Transaction:
    """Transaction record"""
    transaction_id: str
    customer_id: str
    amount: float
    date: datetime
    status: str = "pending"  # Default value
    metadata: Dict = field(default_factory=dict)  # Mutable default
    
    def __post_init__(self):
        """Called after __init__"""
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
    
    def is_large(self) -> bool:
        """Check if large transaction"""
        return self.amount > 10000

# Usage
txn = Transaction(
    transaction_id="TXN001",
    customer_id="CUST123",
    amount=15000.00,
    date=datetime.now()
)

print(txn.is_large())  # True
print(txn)  # Nice repr automatically

# FROZEN DATACLASS (immutable)
@dataclass(frozen=True)
class Config:
    """Immutable configuration"""
    database_url: str
    max_connections: int
    timeout: float

config = Config("postgresql://localhost", 10, 30.0)
# config.timeout = 60  # Error! Frozen

# Use in PySpark
from pyspark.sql import Row

def dict_to_transaction(d: dict) -> Transaction:
    return Transaction(**d)

# Convert Spark rows to dataclass
rdd_of_transactions = spark_df.rdd.map(lambda row: dict_to_transaction(row.asDict()))
```

---

### **Evening: 7:00-7:30 (30 min) - ML Pipeline Foundation**

```python
# Conceptual: PySpark + sklearn integration
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier

# Feature engineering in PySpark (big data)
assembler = VectorAssembler(
    inputCols=["feature1", "feature2", "feature3"],
    outputCol="features"
)

df_vectorized = assembler.transform(df)

# Train model in PySpark ML
rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="label",
    numTrees=100
)

model = rf.fit(df_vectorized)

# Make predictions
predictions = model.transform(df_test)
```

- [ ] Read: "PySpark ML vs sklearn" comparison
- [ ] When to use which library?

---

# **DAYS 4-10: CONTINUE PATTERN**

**I'll provide the detailed structure for Days 4-10 based on the same format:**

**DAY 4:** PySpark UDFs + Python Concurrency (threading, multiprocessing)
**DAY 5:** PySpark Streaming + Python Async/Await
**DAY 6:** Delta Lake + MLflow Integration
**DAY 7:** PySpark SQL + Advanced sklearn
**DAY 8:** Feature Engineering + Model Deployment
**DAY 9:** End-to-End AI Pipeline Project
**DAY 10:** Mock Interviews + Review

Would you like me to:
1. **Continue with full Days 4-10 breakdown** (similar detail)
2. **Jump to specific days you're most interested in**
3. **Focus on a specific area** (e.g., "Deep dive on PySpark streaming" or "Advanced ML deployment")

Let me know and I'll provide the rest! 🚀

For now, **START DAY 1 TOMORROW** - it's perfectly structured for your goals! 💪
