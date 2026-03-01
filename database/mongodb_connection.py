import sys
import time
from pathlib import Path

from pymongo import MongoClient
from pymongo.errors import AutoReconnect, ConnectionFailure, ServerSelectionTimeoutError

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from config.database_config import COLLECTION_NAME, DATABASE_NAME, MONGODB_URI

MAX_RETRIES = 5
BASE_DELAY = 2


def get_client() -> MongoClient:
    last_error = None

    for attempt in range(MAX_RETRIES):
        try:
            client = MongoClient(
                MONGODB_URI,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=5000,
                socketTimeoutMS=5000,
            )
            client.admin.command("ping")
            return client
        except (ServerSelectionTimeoutError, AutoReconnect, ConnectionFailure) as exc:
            last_error = exc
            if attempt == MAX_RETRIES - 1:
                break
            wait_seconds = BASE_DELAY ** (attempt + 1)
            print(f"MongoDB connection failed. Retrying in {wait_seconds}s...")
            time.sleep(wait_seconds)

    raise RuntimeError("MongoDB connection failed after multiple retries") from last_error


def get_collection():
    client = get_client()
    db = client[DATABASE_NAME]
    return db[COLLECTION_NAME]


def test_connection() -> None:
    try:
        get_client()
        print("MongoDB connection successful")
    except Exception as exc:
        print(f"MongoDB connection failed: {exc}")


if __name__ == "__main__":
    test_connection()
