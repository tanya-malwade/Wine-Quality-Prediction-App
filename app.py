import streamlit as st
import numpy as np
import joblib

# Load model & scaler
model = joblib.load("wine_model.joblib")
scaler = joblib.load("scaler.joblib")

st.set_page_config(page_title="Wine Quality Prediction", layout="centered")

st.title("🍷 Wine Quality Prediction App")

st.write("Enter wine chemical properties to predict quality")

# Inputs
fixed_acidity = st.number_input("Fixed Acidity", 0.0, 20.0, 7.4)
volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0, 0.7)
citric_acid = st.number_input("Citric Acid", 0.0, 1.0, 0.0)
residual_sugar = st.number_input("Residual Sugar", 0.0, 20.0, 1.9)
chlorides = st.number_input("Chlorides", 0.0, 1.0, 0.076)
free_sulfur = st.number_input("Free Sulfur Dioxide", 0, 100, 11)
total_sulfur = st.number_input("Total Sulfur Dioxide", 0, 300, 34)
density = st.number_input("Density", 0.9900, 1.0100, 0.9978)
pH = st.number_input("pH", 2.0, 4.5, 3.51)
sulphates = st.number_input("Sulphates", 0.0, 2.0, 0.56)
alcohol = st.number_input("Alcohol", 8.0, 15.0, 9.4)

if st.button("Predict Quality"):
    data = np.array([[fixed_acidity, volatile_acidity, citric_acid,
                      residual_sugar, chlorides, free_sulfur,
                      total_sulfur, density, pH, sulphates, alcohol]])
    
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)

    st.success(f"Predicted Wine Quality: {round(prediction[0], 2)}")
