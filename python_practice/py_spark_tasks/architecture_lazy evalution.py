## Ad-hoc analysis, Unit testing, and Scheduled Batch jobs

'''
 Architecture & Lazy Evaluation

 Concept: Understanding that code only runs when an Action is called.

The Task: Create a massive DataFrame by joining two sample datasets. Perform 5 transformations (filter, select, withColumn).

Challenge: Observe the "Spark UI" (Jobs tab). Does Spark run the code when you define the transformations? Now, call .count(). 
What changed in the UI? Explain why count() is an "Action" and filter() is a "Transformation."

The Transformations (Lazy Steps)

Join: Connect ecommerce_orders_delta and silver_customers using a common ID (like customer_id).
Filter: Filter for orders from a specific date range or region.
WithColumn: Create a total_with_tax column by multiplying the price by 1.15.
Lower: Use lower() on the customer names to standardize them.
Select: Keep only the final 5 columns you actually need.

The Action (The Trigger)

Run the code. Check the Spark UI. You will see 0 Jobs.
Now, call .count().
What changed? Suddenly, a "Job" appears in the UI. Spark had to actually scan the Delta files and the Silver table files to give you that number.
'''
from pyspark.sql.functions import lower, col
from pyspark.sql.types import IntegerType,StringType

# In Databricks, the 'spark' variable is already globally available.
# We skip the builder and the .stop() to keep the session alive.

def apply_transformations(df1, df2):
    # Transformation (Lazy)
    merged_data = df1.join(
        df2, 
        (col("user_id").cast(StringType()) == col("customer_key").cast(StringType())), 
        how="inner"
    )
    merged_data = merged_data.filter(col("region") == "Indiana")
    merged_data = merged_data.withColumn("total_with_tax", col("price_per_unit") * 1.15)
    
    return merged_data.select(
        lower(col("full_name")).alias("standard_name"),
        "total_with_tax",
        "region"
    ).limit(5)

spark = SparkSession.
# 1. Access Tables
df_orders = spark.table("default.ecommerce_orders_delta")
df_customers = spark.table("default.silver_customers")

# 2. Apply Logic
final_df = apply_transformations(df_orders, df_customers)

# 3. Trigger Actions
print("Results from Indiana:")
final_df.show(truncate=False)

print("Physical Execution Plan:")
final_df.explain()
