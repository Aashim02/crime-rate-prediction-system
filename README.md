# Crime Rate Prediction System

End-to-end project scaffold for crime-rate prediction with MongoDB storage, Spark processing, ML modeling, anomaly detection, API endpoints, and Flutter mobile alert UI placeholders.

## Project Modules

- `database/` MongoDB connection and data I/O
- `scripts/` setup and environment validation helpers
- `spark_processing/` Spark session, cleaning, and feature engineering
- `models/` model training and evaluation
- `anomaly_detection/` Isolation Forest workflow
- `api/` Flask app with prediction and alert endpoints
- `frontend/` simple web UI for prediction requests
- `mobile_app/crime_alert_app/` Flutter starter app
- `notebooks/` exploratory analysis notebook

## Quick Start

1. Create and activate your virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Start MongoDB locally.
4. Train a model and run pipeline:
   - `python main.py`
5. Run API:
   - `python api/app.py`
6. Open web frontend:
   - `frontend/index.html`

## MongoDB Setup (Windows)

1. Download MongoDB Community Server (MSI):
   - https://www.mongodb.com/try/download/community
2. Install with **Complete Setup** and **Install MongoDB as a Service**.
3. Start service from Command Prompt:
   - `net start MongoDB`
4. Verify connection:
   - `python database/mongodb_connection.py`
   - Expected: `MongoDB connected successfully`

## MongoDB Atlas on AWS (Recommended)

1. Create Atlas account and cluster on AWS:
   - https://www.mongodb.com/cloud/atlas
2. Create DB user and allow network access (`0.0.0.0/0` for development only).
3. Copy your Atlas connection string from `Connect -> Drivers`.
4. Configure environment variables (recommended):
   - `MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority`
   - `MONGODB_DATABASE=crime_db`
   - `MONGODB_COLLECTION=crime_data`
5. Test cloud connection:
   - `python database/mongodb_connection.py`
   - Expected: `Connected to MongoDB Atlas successfully`
6. Upload dataset:
   - `python database/insert_data.py`

Use `.env.example` as reference and keep real credentials out of Git.

## Automatic .env Loading (python-dotenv)

This project auto-loads variables from `.env` in `config/database_config.py` and `spark_processing/spark_session.py`.

1. Create `.env` in project root (already scaffolded):

```env
MONGODB_URI=mongodb+srv://crimeadmin:password@crime-cluster.mongodb.net/?retryWrites=true&w=majority
MONGODB_DATABASE=crime_db
MONGODB_COLLECTION=crime_data
```

2. Install dependencies:

- `pip install -r requirements.txt`

3. Run without manual environment exports:

- `python scripts/check_env.py`
- `python database/mongodb_connection.py`
- `python database/insert_data.py`
- `python main.py`
- `python api/app.py`

Use `python scripts/check_env.py` before pipeline/API runs to catch URI, DNS, and credential issues early.

Expected MongoDB check output:

- `MongoDB connection successful`
- or `MongoDB connection failed: ...` (if URI/network credentials are not yet valid)

Security note:

- `.env` is excluded via `.gitignore` and should never be committed.

## Spark with Atlas (Optional)

To pass MongoDB URI into Spark session, set:

- `SPARK_MONGO_READ_URI=mongodb+srv://<username>:<password>@<cluster-url>/crime_db.crime_data`

Then start your pipeline as usual with `python main.py`.

## API Endpoints

- `POST /predict`
- `POST /predict_crime`
- `POST /crime_alert`
- `GET /health`

## Frontend Payload Example

The web UI sends:

```json
{
  "crime_type": 1,
  "area": 2,
  "time": 3,
  "month": 5
}
```

Expected response:

```json
{
  "prediction": "High Crime Risk"
}
```

## Suggested Extensions

- Python
- Pylance
- Jupyter
- MongoDB for VS Code
- Flutter

## Deploy on Render

1. Push this repository to GitHub.
2. Create a new **Web Service** in Render from this repository.
3. Use these settings:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python api/app.py` (or use included `Procfile`)
   - **Branch:** `main`
4. Add environment variables in Render:
   - `MONGODB_URI`
   - `MONGODB_DATABASE=crime_db`
   - `MONGODB_COLLECTION=crime_data`
5. Deploy and verify:
   - `GET /health` should return `{"status":"API running"}`

### Frontend API URL for Cloud

In browser console (or inline script), set:

```js
window.API_BASE_URL = "https://<your-render-service>.onrender.com";
```

Then the frontend will call cloud API endpoints automatically.

### Spark Note for Render

Render free/starter environments are not ideal for heavy Spark jobs. Keep Spark preprocessing for local/offline runs (`python main.py`) and use the trained model for API predictions in production.
