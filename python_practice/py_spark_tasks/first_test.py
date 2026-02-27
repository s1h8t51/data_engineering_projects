from pyspark.sql import SparkSession
import os

# Initialize Spark
spark = SparkSession.builder \
    .appName("CodespaceTest") \
    .getOrCreate()

# Create dummy data
data = [("GitHub Codespaces", "Ready"), ("Java 17", "Active"), ("Python 3.12", "Active")]
df = spark.createDataFrame(data, ["Component", "Status"])

# Show the result
df.show()

print(f"JAVA_HOME is set to: {os.environ.get('JAVA_HOME')}")