from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from config.database_config import MONGODB_URI
from database.mongodb_connection import get_collection


def insert_csv_to_mongodb(csv_path: Path) -> int:
    df = pd.read_csv(csv_path)
    records = df.to_dict(orient="records")
    if not records:
        return 0

    collection = get_collection()
    result = collection.insert_many(records)
    return len(result.inserted_ids)


if __name__ == "__main__":
    try:
        inserted = insert_csv_to_mongodb(Path("data/raw/crime_data.csv"))
        target = "MongoDB Atlas" if MONGODB_URI.startswith("mongodb+srv://") else "MongoDB"
        print(f"Crime dataset inserted successfully ({inserted} records to {target})")
    except Exception as exc:
        print(f"Crime dataset insertion failed: {exc}")
