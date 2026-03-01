from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim


def clean_crime_data(df: DataFrame) -> DataFrame:
    cleaned_df = df.dropna()
    if "crime_type" in cleaned_df.columns:
        cleaned_df = cleaned_df.withColumn("crime_type", trim(col("crime_type")))
    return cleaned_df
