import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("BP_Stage_Predictor.pkl")

# Title
st.title("🩺 Blood Pressure Stage Prediction")

# Define stages with explanation & medical advice
stage_dict = {
    0: {
        "name": "Normal",
        "meaning": "Ideal blood pressure.",
        "attention": "✅ No immediate concern. Maintain a healthy lifestyle."
    },
    1: {
        "name": "Elevated",
        "meaning": "Above normal, but not high.",
        "attention": "⚠️ Start monitoring BP regularly. Adopt healthier diet and exercise."
    },
    2: {
        "name": "Stage 1 Hypertension",
        "meaning": "Mild high blood pressure.",
        "attention": "⚠️ Requires lifestyle changes and possibly medications. Regular checkups needed."
    },
    3: {
        "name": "Stage 2 Hypertension",
        "meaning": "Moderate to severe hypertension.",
        "attention": "🚨 Needs medical intervention. Strict medication, diet, and monitoring."
    },
    4: {
        "name": "Hypertensive Crisis",
        "meaning": "Extremely high BP.",
        "attention": "🚑 Seek emergency care immediately!"
    }
}

# Helper to convert Yes/No to binary
def yes_no_to_binary(value):
    return 1 if value == "Yes" else 0

# Input Form
st.header("Enter Patient Information")

history = yes_no_to_binary(st.selectbox("📋 History of BP? (Previously diagnosed with high BP?)", ["No", "Yes"]))
patient = yes_no_to_binary(st.selectbox("🧾 Diagnosed with BP? (Doctor confirmed high blood pressure?)", ["No", "Yes"]))
takemedication = yes_no_to_binary(st.selectbox("💊 Taking Medication? (Currently on BP medicines?)", ["No", "Yes"]))
breathshortness = yes_no_to_binary(st.selectbox("😮‍💨 Breath Shortness? (Experiencing breathlessness?)", ["No", "Yes"]))
visualchanges = yes_no_to_binary(st.selectbox("👀 Visual Changes? (Blurred or double vision?)", ["No", "Yes"]))
nosebleeding = yes_no_to_binary(st.selectbox("🤧 Nose Bleeding? (Frequent or unexplained nosebleeds?)", ["No", "Yes"]))

systolic = st.slider("🔼 Systolic BP (Top number – pressure during heartbeat)", 80, 200, 120)
diastolic = st.slider("🔽 Diastolic BP (Bottom number – pressure between beats)", 50, 140, 80)

controlleddiet = yes_no_to_binary(st.selectbox("🥗 On Controlled Diet? (Following BP-friendly diet?)", ["No", "Yes"]))
c_Male = yes_no_to_binary(st.selectbox("👤 Gender", ["Female", "Male"]))

# Age group
age_group = st.selectbox("📆 Age Group", ["<35", "35–50", "51–64", "65+"])
age_35_50 = 1 if age_group == "35–50" else 0
age_51_64 = 1 if age_group == "51–64" else 0
age_65 = 1 if age_group == "65+" else 0

# Diagnosis timing
diagnosed_when = st.selectbox("🕒 When Diagnosed with BP?", ["<1 year ago", "1–5 years ago", ">5 years ago"])
whendiagnoused_1year = 1 if diagnosed_when == "<1 year ago" else 0
whendiagnoused_5years = 1 if diagnosed_when == ">5 years ago" else 0

# Pulse Pressure
pulse_pressure = systolic - diastolic

# Prediction
if st.button("🔍 Predict Stage"):
    input_data = np.array([[
        history, patient, takemedication, breathshortness, visualchanges,
        nosebleeding, systolic, diastolic, controlleddiet, c_Male,
        age_35_50, age_51_64, age_65, whendiagnoused_1year,
        whendiagnoused_5years, pulse_pressure
    ]])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]
    confidence = np.max(proba) * 100

    stage_info = stage_dict.get(prediction, {
        "name": "Unknown", "meaning": "Not defined", "attention": "⚠️ Consult a doctor."
    })

    st.success(f"✅ **Predicted Stage: {stage_info['name']}**")
    st.write(f"📖 **Meaning:** {stage_info['meaning']}")
    st.warning(f"👨‍⚕️ **Recommended Action:** {stage_info['attention']}")
    st.info(f"🔒 Model Confidence: **{confidence:.2f}%**")
