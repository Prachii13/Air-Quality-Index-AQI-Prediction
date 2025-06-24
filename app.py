import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("🌫️ AQI Predictor")

cols = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
values = {c: st.number_input(c, min_value=0.0, value=10.0) for c in cols}

if st.button("Predict AQI"):
    df = pd.DataFrame([values])
    pred = model.predict(df)[0]
    st.success(f"🌫️ Predicted AQI: {pred:.2f}")
