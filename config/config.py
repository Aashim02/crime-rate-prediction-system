from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "crime_data.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "cleaned_crime_data.csv"
MODEL_PATH = BASE_DIR / "models" / "crime_prediction_model.pkl"

SPARK_APP_NAME = "CrimePrediction"
SPARK_MASTER = "local[*]"
