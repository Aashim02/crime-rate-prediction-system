from pathlib import Path
import sys

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from config.config import MODEL_PATH, PROCESSED_DATA_PATH


FEATURES = ["location", "crime_type", "incident_count"]
TARGET = "target_high_risk"


def build_model(model_type: str = "random_forest") -> Pipeline:
    categorical_features = ["location", "crime_type"]
    numeric_features = ["incident_count"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", StandardScaler(), numeric_features),
        ]
    )

    if model_type == "logistic_regression":
        estimator = LogisticRegression(max_iter=1000)
    else:
        estimator = RandomForestClassifier(n_estimators=200, random_state=42)

    return Pipeline(steps=[("preprocessor", preprocessor), ("model", estimator)])


def train_and_save(model_type: str = "random_forest", model_path: Path = MODEL_PATH) -> Path:
    df = pd.read_csv(PROCESSED_DATA_PATH)
    x = df[FEATURES]
    y = df[TARGET]

    x_train, _, y_train, _ = train_test_split(x, y, test_size=0.2, random_state=42)
    pipeline = build_model(model_type=model_type)
    pipeline.fit(x_train, y_train)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, model_path)
    return model_path


if __name__ == "__main__":
    path = train_and_save()
    print(f"Saved model to {path}")
