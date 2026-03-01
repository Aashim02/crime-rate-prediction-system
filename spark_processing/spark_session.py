import os

from dotenv import load_dotenv
from pyspark.sql import SparkSession

from config.config import SPARK_APP_NAME, SPARK_MASTER

load_dotenv()


def get_spark_session() -> SparkSession:
    builder = SparkSession.builder.appName(SPARK_APP_NAME).master(SPARK_MASTER)

    mongo_read_uri = os.getenv("SPARK_MONGO_READ_URI")
    if mongo_read_uri:
        builder = builder.config("spark.mongodb.read.connection.uri", mongo_read_uri)

    return builder.getOrCreate()
