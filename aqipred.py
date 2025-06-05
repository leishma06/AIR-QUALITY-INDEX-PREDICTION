import streamlit as st
import pickle
import numpy as np

# Load model
file = open(r"C:\Users\leish\python\model.pkl", 'rb') 
model = pickle.load(file)

# Page configuration
st.set_page_config(page_title="Air Pollution Predictor", layout="centered")

# Custom CSS (Dark + Green Theme with Lighting)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0b0f0c;
    color: #e0f7e9;
}

h1, h2, h3, h4 {
    color: #9effc2;
    text-align: center;
    text-shadow: 0 0 5px #00ff88;
}

.stApp {
    padding: 2rem 1rem;
    background: linear-gradient(135deg, #0b0f0c 0%, #102418 100%);
    border-radius: 12px;
    box-shadow: 0 0 20px #00ff88;
}

input[type=number], .stTextInput > div > div > input {
    background-color: #1c2b20;
    color: #9effc2;
    border-radius: 5px;
    border: 1px solid #00ff88;
}

button {
    background-color: #1a3d2c !important;
    color: white !important;
}

.air-quality {
    text-align: center;
    font-size: 1.5rem;
    margin-top: 1rem;
    font-weight: 600;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(to right, transparent, #00ff88, transparent);
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌿 Air Pollution Predictor")

# Introduction Section
st.markdown("""
### 🌫️ What is Air Pollution?
Air pollution refers to the presence of harmful substances in the air we breathe. These pollutants — such as **SO₂**, **NO₂**, **CO**, **O₃**, and **PM particles** — can affect human health, wildlife, and the climate.

Major contributors include:
- Vehicular and industrial emissions
- Construction dust and waste burning
- Agricultural and chemical processes

---

### 🧠 About This Model
This machine learning model has been trained using real air quality data. Based on various input parameters like **SO₂**, **CO**, **NOₓ**, **NH₃**, wind, and temperature, it predicts a corresponding **Air Quality Index (AQI)** score and classifies the air quality into categories such as:

- **Good (0–50)**
- **Moderate (51–100)**
- **Poor (101 and above)**

---
""")

# Inputs
st.markdown("### 📊 Enter Air Quality Parameters")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("SO₂ (μg/m³)", min_value=0.0)
    b = st.number_input("CO (mg/m³)", min_value=0.0)
    c = st.number_input("NO (μg/m³)", min_value=0.0)
    d = st.number_input("NO₂ (μg/m³)", min_value=0.0)
    e = st.number_input("NOₓ (μg/m³)", min_value=0.0)
    f = st.number_input("NH₃ (μg/m³)", min_value=0.0)

with col2:
    g = st.number_input("O₃ (μg/m³)", min_value=0.0)
    h = st.number_input("Wind Speed (WS)", min_value=0.0)
    i = st.number_input("Wind Direction (WD)", min_value=0.0)
    j = st.number_input("Relative Humidity (RH)", min_value=0.0)
    k = st.number_input("Solar Radiation (SR)", min_value=0.0)
    l = st.number_input("Temperature (TC)", min_value=0.0)

# Prediction
if st.button("🔍 Predict AQI"):
    input_data = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
    result = model.predict(input_data)
    st.success(f"✅ Predicted AQI Value: {result[0]:.2f}")

    if result <= 50:
        label = "Good"
        color = "#00ff88"
    elif result <= 100:
        label = "Moderate"
        color = "#ffaa00"
    else:
        label = "Poor"
        color = "#ff4444"

    st.markdown(f"<div class='air-quality' style='color:{color}'>Air Quality: {label}</div>", unsafe_allow_html=True)