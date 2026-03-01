import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from anomaly_detection.anomaly_model import train_isolation_forest
from config.config import RAW_DATA_PATH


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    model = train_isolation_forest(df)
    result = df.copy()
    result["anomaly_flag"] = model.predict(df[["incident_count"]])
    result["anomaly_flag"] = result["anomaly_flag"].map({1: 0, -1: 1})
    return result


if __name__ == "__main__":
    frame = pd.read_csv(RAW_DATA_PATH)
    detected = detect_anomalies(frame)
    print(f"Anomalies detected: {int(detected['anomaly_flag'].sum())} records")
