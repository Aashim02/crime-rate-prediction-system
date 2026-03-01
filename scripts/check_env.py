import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

uri = os.getenv("MONGODB_URI")
database = os.getenv("MONGODB_DATABASE")
collection = os.getenv("MONGODB_COLLECTION")

print("\nChecking environment configuration...\n")

if not uri:
    print("ERROR: MONGODB_URI not set in .env")
    sys.exit(1)

if not database:
    print("ERROR: MONGODB_DATABASE not set")
    sys.exit(1)

if not collection:
    print("ERROR: MONGODB_COLLECTION not set")
    sys.exit(1)

print("Environment variables found")

atlas_pattern = r"^mongodb\+srv://"
if not re.match(atlas_pattern, uri):
    print("WARNING: URI may not be a MongoDB Atlas URI")
else:
    print("Atlas URI format looks correct")

try:
    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000,
        socketTimeoutMS=5000,
    )
    client.admin.command("ping")
    print("MongoDB Atlas connection successful")
except Exception as exc:
    print("MongoDB connection failed")
    print(f"Reason: {exc}")

print("\nEnvironment check completed\n")
