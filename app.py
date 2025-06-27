import streamlit as st
from ai_model.inference import get_medical_analysis

st.title("🩺 AI Medical Lab Report Analyzer")

# User Inputs
gender = st.selectbox("Select Gender", ["Male", "Female"])
hb = st.number_input("Hemoglobin (g/dL)", min_value=0.0, step=0.1)
wbc = st.number_input("WBC (per mm³)", min_value=0)
platelet = st.number_input("Platelet Count (per µL)", min_value=0)
esr = st.number_input("ESR (mm/hr)", min_value=0)
sugar = st.number_input("Fasting Blood Sugar (mg/dL)", min_value=0)

# When button is clicked
if st.button("Analyze"):
    result = get_medical_analysis(gender,hb, wbc, platelet, esr, sugar)
    st.markdown("### 🧠 AI Medical Insight")
    st.markdown(result)


