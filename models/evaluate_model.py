import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

from config.config import MODEL_PATH, PROCESSED_DATA_PATH
from models.train_model import FEATURES, TARGET


def evaluate() -> dict:
    df = pd.read_csv(PROCESSED_DATA_PATH)
    x = df[FEATURES]
    y_true = df[TARGET]

    pipeline = joblib.load(MODEL_PATH)
    y_pred = pipeline.predict(x)

    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "report": classification_report(y_true, y_pred, zero_division=0),
    }


if __name__ == "__main__":
    metrics = evaluate()
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(metrics["report"])
