from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder, Imputer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import pyspark.sql.functions as F

class BNSFSparkPredictor:
    def __init__(self, target_col="delayed"):
        self.target_col = target_col
        self.pipeline_model = None
        self.metrics_df = None

    def prepare_data(self, df):
        """PART 1: Robust Feature Engineering"""
        
        # 1. Fill zeros to avoid division by zero errors
        df = df.fillna(0, subset=["cargo_weight_tons", "locomotive_age_years"])

        # 2. Create features with Null-safety
        df = df.withColumn("distance_per_ton", F.col("distance_miles") / (F.col("cargo_weight_tons") + 0.1)) \
               .withColumn("maintenance_per_age", F.col("maintenance_score") / (F.col("locomotive_age_years") + 0.1))
        
        # 3. Impute ALL numeric columns used in features
        # We add the new calculated columns here too just in case!
        numeric_cols = ["distance_miles", "cargo_weight_tons", "maintenance_score", 
                        "crew_experience_years", "distance_per_ton", "maintenance_per_age"]
        
        imputer = Imputer(
            inputCols=numeric_cols, 
            outputCols=numeric_cols,
            strategy="median"
        )

        # 4. Categorical Encoding (Add handleInvalid="keep" to be safe)
        stages = [imputer]
        cat_cols = ['route', 'weather_condition']
        
        for col in cat_cols:
            indexer = StringIndexer(inputCol=col, outputCol=f"{col}_idx", handleInvalid="keep")
            encoder = OneHotEncoder(inputCol=f"{col}_idx", outputCol=f"{col}_vec")
            stages += [indexer, encoder]

        # 5. Assemble Features
        feature_cols = numeric_cols + [f"{c}_vec" for c in cat_cols]
        
        # We set handleInvalid="skip" here as a fail-safe backup
        assembler = VectorAssembler(inputCols=feature_cols, outputCol="features", handleInvalid="skip")
        stages.append(assembler)

        return df, stages
    
    def train_delay_predictor(self, df, stages):
        """PART 2: Model Training & Evaluation"""
        # Stratified Split (Approximate in Spark)
        train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

        models = {
            "LogisticReg": LogisticRegression(featuresCol="features", labelCol=self.target_col),
            "RandomForest": RandomForestClassifier(featuresCol="features", labelCol=self.target_col, numTrees=100)
        }

        results = []
        evaluator = MulticlassClassificationEvaluator(labelCol=self.target_col, predictionCol="prediction")
        
        best_f1 = 0
        
        for name, model in models.items():
            # Create a full pipeline for each model
            current_pipeline = Pipeline(stages=stages + [model])
            fit_model = current_pipeline.fit(train_df)
            predictions = fit_model.transform(test_df)

            # Metrics
            metrics = {
                "model_name": name,
                "accuracy": evaluator.evaluate(predictions, {evaluator.metricName: "accuracy"}),
                "f1_score": evaluator.evaluate(predictions, {evaluator.metricName: "f1"}),
                "precision": evaluator.evaluate(predictions, {evaluator.metricName: "weightedPrecision"}),
                "recall": evaluator.evaluate(predictions, {evaluator.metricName: "weightedRecall"})
            }
            results.append(metrics)

            if metrics["f1_score"] > best_f1:
                best_f1 = metrics["f1_score"]
                self.pipeline_model = fit_model

        self.metrics_df = spark.createDataFrame(results)
        return self.pipeline_model, self.metrics_df

    def predict_batch(self, new_df):
        """PART 3: Production Inference"""
        # Apply the SAME feature engineering logic
        processed_df, _ = self.prepare_data(new_df)
        
        # Inference using the trained PipelineModel
        predictions = self.pipeline_model.transform(processed_df)

        # Extract "Confidence" from the probability vector
        # (Spark probability is a vector [prob_0, prob_1])
        get_prob = F.udf(lambda v: float(v[1]), "float")
        
        final_df = predictions.withColumn("confidence", get_prob(F.col("probability"))) \
            .withColumn("risk_level", F.when(F.col("confidence") > 0.7, "High Risk").otherwise("Standard")) \
            .select("train_id", "prediction", "confidence", "risk_level")

        # Summary Stats
        summary = {
            "total_trains": final_df.count(),
            "predicted_delays": int(final_df.filter(F.col("prediction") == 1).count()),
            "high_risk_count": int(final_df.filter(F.col("risk_level") == "High Risk").count()),
            "avg_confidence": final_df.select(F.avg("confidence")).first()[0]
        }

        return final_df, summary
    
    # 1. Initialize the Predictor
# Load the raw data
# Use the 'file:' prefix to tell Databricks to look in the local node's workspace
import pandas as pd
import pandas as pd

# 1. The absolute path to your file in the Workspace
file_path = "/Workspace/Users/sahityagantalausa@gmail.com/data_engineering_projects/train_delays.csv"

# 2. Read with Pandas (Python can see this path even if Spark Workers can't)
pdf = pd.read_csv(file_path)

# 3. Convert to Spark DataFrame
raw_df = spark.createDataFrame(pdf)

# 4. Verify
raw_df.show(5)


# 1. Initialize the Class
predictor = BNSFSparkPredictor(target_col="delayed")

# 2. Part 1: Feature Engineering & Preprocessing
# This handles the NULLs and encodes categorical strings (route, weather)
df_with_features, ml_stages = predictor.prepare_data(raw_df)

# 3. Part 2: Model Training & Comparison
# Trains Logistic Regression vs. Random Forest and returns the metrics
best_pipeline, metrics_df = predictor.train_delay_predictor(df_with_features, ml_stages)

print("--- Step 2: Model Performance Comparison ---")
metrics_df.show()

# 4. Part 3: Production Inference (The High-Risk Flags)
# This gives you the 'Confidence' and 'Risk Level' Shahzeb wants
results_df, summary = predictor.predict_batch(raw_df)

print("--- Step 3: High-Risk Predictions ---")
results_df.sort(F.col("confidence").desc()).show(10)

print("--- Executive Summary Stats ---")
import json
print(json.dumps(summary, indent=4))

