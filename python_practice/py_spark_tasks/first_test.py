
'''
Spark Mastery: 10 Hands-on Tasks

Task 1: Architecture & Lazy Evaluation (Phase 1)

Concept: Understanding that code only runs when an Action is called.

The Task: Create a massive DataFrame by joining two sample datasets. Perform 5 transformations (filter, select, withColumn).

Challenge: Observe the "Spark UI" (Jobs tab). Does Spark run the code when you define the transformations? Now, call .count(). What changed in the UI? Explain why count() is an "Action" and filter() is a "Transformation."

Task 2: The "Only Correct Way" to Ingest (Phase 3)

Concept: Schema Inference vs. Explicit Schema.

The Task: Ingest the customers.csv file two ways:

Using inferSchema=True.

Using a StructType (Explicit Schema) where you define customer_id as a Long and email as a String.

Challenge: Compare the execution time in the Spark UI. Why is the Explicit Schema faster? (Hint: Spark doesn't have to read the file twice).

Task 3: Narrow vs. Wide Transformations (Phase 4 & 5)

Concept: Understanding the "Shuffle."

The Task: Create a notebook that performs a filter() (Narrow) and a groupBy() (Wide).

Challenge: Look at the DAG (Directed Acyclic Graph) in the Spark UI. Why does groupBy create a new "Stage" but filter does not? Explain the "Shuffle" in your own words.

Task 4: Mastering the Shuffle Join (Phase 5)

Concept: Broadcast vs. Shuffle Hash Join.

The Task: Join a large dataset (Retail Orders) with a small dataset (Store Locations).

Challenge: Force a Broadcast Join using broadcast(small_df). Now, disable broadcasting and run it as a regular join. Which is faster? Why is broadcasting a "cheat code" for performance?

Task 5: Data Movement Control (Phase 5)

Concept: repartition vs. coalesce.

The Task: Take a DataFrame and use .repartition(100). Check the number of files written to disk. Now, use .coalesce(1) to bring it back.

Challenge: When would an ERP Manager use coalesce before saving a final report? When would they use repartition for a massive migration?

Task 6: Window Functions for ERP Analytics (Phase 6)

Concept: Advanced Analytics without Shuffles.

The Task: Use the products dataset. For each category, find the top 3 most expensive products using row_number() and Window.partitionBy().

Challenge: Compare this to doing a groupBy and max. Why are Window functions better for keeping row-level detail?

Task 7: The UDF Performance Trap (Phase 7)

Concept: Python ↔ JVM boundary cost.

The Task: Write a Python function to capitalize a string. Apply it to a column using a udf(). Then, do the same thing using the built-in Spark upper() function.

Challenge: Time both operations on 1 million rows. Why is the built-in function 10x faster?

Task 8: Committing Data Safely (Phase 8)

Concept: Write Modes & Atomicity.

The Task: Experiment with mode("append"), mode("overwrite"), and mode("errorIfExists").

Challenge: Simulate a "Job Failure" mid-write. How does Delta Lake ensure that you don't end up with "Half-written" data? (The Transaction Log).

Task 9: Managed vs. External Tables (Phase 9)

Concept: Ownership and Data Risks.

The Task: 1. Create a Managed Table using CTAS.
2. Create an External Table by specifying a LOCATION.

Challenge: Run DROP TABLE on both. Go to the file system (S3/DBFS). Which data disappeared? Which data stayed? Why does a Master Data Manager prefer External tables for raw data?

Task 10: Structured Streaming Fundamentals (Phase 10)

Concept: Micro-batches.

The Task: Set up a readStream on a folder. Drop a new CSV file into that folder.

Challenge: Use .writeStream with trigger(once=True). Explain why "Streaming" in Spark is actually just "Incremental Batching."
'''