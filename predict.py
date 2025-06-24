import joblib
import pandas as pd

model = joblib.load("model.pkl")

sample = {
    "PM2.5": [80],
    "PM10": [160],
    "NO2": [40],
    "SO2": [15],
    "CO": [1.2],
    "O3": [25]
}

df = pd.DataFrame(sample)
prediction = model.predict(df)[0]
print(f"🌫️ Predicted AQI: {prediction:.2f}")
