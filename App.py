import streamlit as st
import joblib
import numpy as np

model = joblib.load('aqi_model.pkl')

st.title("Air Quality Index Predictor")

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no2 = st.number_input("NO2")
so2 = st.number_input("SO2")
co = st.number_input("CO")
o3 = st.number_input("O3")

if st.button("Predict AQI"):
    features = np.array([[pm25, pm10, no2, so2, co, o3]])
    prediction = model.predict(features)
    st.success(f"Predicted AQI: {round(prediction[0], 2)}")
