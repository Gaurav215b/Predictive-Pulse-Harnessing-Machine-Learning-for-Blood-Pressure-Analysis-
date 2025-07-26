# 🩺 Blood Pressure Analysis and Stage Prediction

This project uses machine learning to analyze blood pressure data and predict the severity stage of a patient. It includes:

- 📊 Data analysis using Jupyter Notebook
- 🧠 ML model to predict blood pressure stage
- 🌐 Streamlit-based web app for real-time prediction

---

## 📁 Project Structure

```
├── Blood Pressure Analysis.ipynb   # EDA + ML Modeling
├── BP_web.py                       # Streamlit web app
├── patient_data.csv                # Dataset used (https://drive.google.com/file/d/1qYvKqg4w_w4blizSVqmLvwY25m7V7N3_/view)
├── BP_Stage_Prediction.pkl         
├── README.md                       # This file
├── requirements.txt                # Python dependencies
└── .gitignore                      # Files to ignore
```

---

## 🚀 Features

- Predict BP Stage with meaningful output (e.g. **Stage 1 - Mild Hypertension**)
- Display confidence of predictions
- Give attention level suggestions (e.g. “🚨 Critical - Immediate doctor consultation advised”)

---

## 📊 Dataset

- **File**: `patient_data.csv`
- Contains: age, gender, blood pressure levels, symptoms, diagnosis, and medication info.

---

## 🧠 ML Models Used

- XGBXGBoost

Trained to classify patient BP stage using features like:
- Systolic and Diastolic values
- Diagnosis time
- Medication intake
- Symptoms like nose bleeding, breath shortness, etc.

---

## 🌐 How to Run Web App

```bash
pip install -r requirements.txt
streamlit run BP_web.py
```

---

## 📌 Future Enhancements

- Add model explainability (e.g. SHAP or LIME)
- Deploy to cloud (Streamlit Cloud or HuggingFace Spaces)
- Add history tracker for patient visits

---

## 📄 License

This project is for educational purposes only.
