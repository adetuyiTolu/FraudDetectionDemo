from joblib import load
import pandas as pd
import os

model = load(os.path.join(os.path.dirname(__file__), "risk_predictor.joblib"))


def predict(email, amount):
    is_temp_email = int(email.endswith("tempmail.com"))
    features = pd.DataFrame([{"amount": amount, "is_temp_email": is_temp_email}])
    prediction = model.predict(features)[0]
    return "high" if prediction == 1 else "low"
