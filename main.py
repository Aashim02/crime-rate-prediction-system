import pandas as pd

from anomaly_detection.detect_anomalies import detect_anomalies
from config.config import PROCESSED_DATA_PATH, RAW_DATA_PATH
from database.insert_data import insert_csv_to_mongodb
from models.train_model import train_and_save
from spark_processing.data_cleaning import clean_crime_data
from spark_processing.feature_engineering import add_time_features
from spark_processing.spark_session import get_spark_session
from utils.logger import get_logger
from visualization.crime_graphs import (
    plot_crime_distribution,
    plot_crime_hotspots,
    plot_crime_trends,
)

logger = get_logger(__name__)


def run_pipeline() -> None:
    print("Loading dataset...")
    df = pd.read_csv(RAW_DATA_PATH)

    try:
        inserted = insert_csv_to_mongodb(RAW_DATA_PATH)
        print(f"MongoDB insertion successful ({inserted} records)")
    except Exception as exc:
        print(f"MongoDB insertion skipped: {exc}")

    spark = get_spark_session()
    spark_df = spark.read.csv(str(RAW_DATA_PATH), header=True, inferSchema=True)
    spark_df = clean_crime_data(spark_df)
    spark_df = add_time_features(spark_df)
    spark_df.toPandas().to_csv(PROCESSED_DATA_PATH, index=False)
    spark.stop()
    print("Spark processing completed")

    model_path = train_and_save(model_type="random_forest")
    print(f"Model trained successfully ({model_path})")

    anomaly_df = detect_anomalies(df)
    print("Anomaly detection completed")

    plot_crime_distribution(df, show=False)
    plot_crime_trends(df, show=False)
    plot_crime_hotspots(df, show=False)
    print("Graphs generated")

    logger.info("Pipeline completed. Anomalies detected: %d", int(anomaly_df["anomaly_flag"].sum()))


if __name__ == "__main__":
    run_pipeline()
