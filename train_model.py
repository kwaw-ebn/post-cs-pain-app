import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path

# === Simulated Training Data ===
data = pd.DataFrame({
    "Surgery_Duration": ["<30min", "30-60min", ">60min", "<30min", ">60min"],
    "Anaesthesia": ["Spinal", "General", "Spinal", "General", "Spinal"],
    "Pain_Score": [3, 7, 5, 8, 2],
    "Pain_Risk": ["Low", "High", "Medium", "High", "Low"]
})

# === Encode categorical columns ===
encoders = {}
for col in ["Surgery_Duration", "Anaesthesia", "Pain_Risk"]:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

# === Train simple model ===
X = data[["Surgery_Duration", "Anaesthesia", "Pain_Score"]]
y = data["Pain_Risk"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# === Save model and encoders ===
model_data = {"model": model, "encoders": encoders}

Path("models").mkdir(exist_ok=True)
with open("models/pain_predictor.pkl", "wb") as f:
    pickle.dump(model_data, f)

print("✅ Model saved successfully at models/pain_predictor.pkl")
