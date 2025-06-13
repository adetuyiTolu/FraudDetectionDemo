import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
import random


def is_risky(email, amount):
    if email.endswith("tempmail.com") and amount > 5000:
        return 2
    elif email.endswith("tempemail.com") or amount > 5000:
        return 1
    else:
        return 0


data = []
for _ in range(1000):
    amount = random.uniform(10, 10000)
    email = random.choice(["user@gmail.com", "fraud@tempmail.com", "legit@yahoo.com"])
    label = is_risky(email, amount)
    data.append((amount, int(email.endswith("tempmail.com")), label))

df = pd.DataFrame(data, columns=["amount", "is_temp_email", "risk"])

print(df)

X = df[["amount", "is_temp_email"]]
y = df["risk"]

model = RandomForestClassifier()
model.fit(X, y)

dump(model, "risk_predictor.joblib")
print("model successfully trained")
