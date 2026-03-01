import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from database.mongodb_connection import get_collection


def fetch_crime_data(limit: int | None = None) -> pd.DataFrame:
    collection = get_collection()
    cursor = collection.find({}, {"_id": 0})
    if limit:
        cursor = cursor.limit(limit)
    return pd.DataFrame(list(cursor))


if __name__ == "__main__":
    df = fetch_crime_data(limit=5)
    print(df.head())
