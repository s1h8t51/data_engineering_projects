## oops inheritance pattern 
from pyspark.sql import functions as F
from pyspark.sql import Window
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml import Pipeline

class TrainDelayPipeline:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def extract(self):
        self.df = spark.read.csv(self.file_path, header=True, inferSchema=True)
        return self.df

    def transform(self):
        # 1. Handling Missing Values (Median calculation)
        for col in ["maintenance_score", "crew_experience_years"]:
            # Calculate median globally first
            median_val = self.df.select(F.percentile_approx(col, 0.5)).first()[0]
            self.df = self.df.withColumn(col, F.coalesce(F.col(col), F.lit(median_val)))

        # 2. Feature Engineering
        self.df = self.df.withColumn("maintenance_per_age", F.col("maintenance_score") / F.col("locomotive_age_years")) \
                         .withColumn("is_heavy_cargo", (F.col("cargo_weight_tons") > 6000).cast("int")) \
                         .withColumn("is_old_locomotive", (F.col("locomotive_age_years") > 15).cast("int"))

        # 3. Drop unnecessary columns
        # Note: We keep 'delayed' as our label
        cols_to_drop = ['train_id', 'actual_duration_hours']
        self.df = self.df.drop(*cols_to_drop)

        # 4. Encoding Categorical Variables (The Spark Way)
        # This replaces pd.get_dummies
        cat_cols = ['route', 'weather_condition']
        stages = []
        for col in cat_cols:
            indexer = StringIndexer(inputCol=col, outputCol=f"{col}_idx")
            encoder = OneHotEncoder(inputCol=f"{col}_idx", outputCol=f"{col}_vec")
            stages += [indexer, encoder]

        # 5. Assemble all features into one Vector (Required for Spark ML)
        feature_cols = [c for c in self.df.columns if c not in cat_cols + ['delayed']] + ["route_vec", "weather_condition_vec"]
        assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
        stages.append(assembler)

        # Run the internal Spark pipeline
        ml_pipeline = Pipeline(stages=stages)
        model_ready_df = ml_pipeline.fit(self.df).transform(self.df)

        return model_ready_df.select("features", "delayed")

class Mlpipeline:

    def model_training(self):
        pass

    def prediction(self):
        pass

ml_dataframe = TrainDelayPipeline(file_path)
final_stats = Mlpipeline(ml_dataframe)
print(final_stats)
