from pathlib import Path

import joblib
import pandas as pd
from flask import Blueprint, jsonify, request

from api.alert_service import build_alert_message
from config.config import MODEL_PATH

prediction_bp = Blueprint("prediction", __name__)

_model = None


def get_model():
    global _model
    if _model is None:
        if not Path(MODEL_PATH).exists() or Path(MODEL_PATH).stat().st_size == 0:
            raise FileNotFoundError("Model file not found or empty. Train model first.")
        _model = joblib.load(MODEL_PATH)
    return _model


@prediction_bp.route("/predict_crime", methods=["POST"])
def predict_crime():
    payload = request.get_json(force=True)
    input_row = pd.DataFrame(
        [
            {
                "location": payload.get("location", "Unknown"),
                "crime_type": payload.get("crime_type", "Unknown"),
                "incident_count": int(payload.get("incident_count", 0)),
            }
        ]
    )

    model = get_model()
    pred = int(model.predict(input_row)[0])
    return jsonify({"prediction": pred})


@prediction_bp.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(force=True)
    crime_type = int(payload.get("crime_type", 0))
    area = int(payload.get("area", 0))
    time = int(payload.get("time", 0))
    month = int(payload.get("month", 0))

    risk_score = crime_type + area + time + month
    label = "High Crime Risk" if risk_score >= 8 else "Low Crime Risk"
    return jsonify({"prediction": label})


@prediction_bp.route("/crime_alert", methods=["POST"])
def crime_alert():
    payload = request.get_json(force=True)
    prediction = int(payload.get("prediction", 0))
    return jsonify({"alert": build_alert_message(prediction)})
