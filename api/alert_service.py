def build_alert_message(prediction: int) -> str:
    if prediction == 1:
        return "High crime risk detected. Please stay alert in this area."
    return "No immediate high-risk signal detected."
