import os

from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("MONGODB_DATABASE", "crime_db")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION", "crime_data")
