from pyspark.sql import DataFrame
from pyspark.sql.functions import col, hour, to_timestamp, when


def add_time_features(df: DataFrame) -> DataFrame:
    if "timestamp" not in df.columns:
        return df

    enriched = df.withColumn("timestamp", to_timestamp(col("timestamp")))
    enriched = enriched.withColumn("hour_of_day", hour(col("timestamp")))
    enriched = enriched.withColumn(
        "night_time",
        when((col("hour_of_day") >= 20) | (col("hour_of_day") < 6), 1).otherwise(0),
    )
    return enriched
