import pandas as pd
from sklearn.ensemble import IsolationForest


def train_isolation_forest(df: pd.DataFrame) -> IsolationForest:
    numeric_cols = [col for col in ["incident_count"] if col in df.columns]
    if not numeric_cols:
        raise ValueError("No numeric columns available for anomaly model training")

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(df[numeric_cols])
    return model
