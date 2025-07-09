import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Eligibility Predictor")

# User input
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.number_input("Loan Term (days)", min_value=0, value=360)

# Prediction
if st.button("Check Eligibility"):
    df = pd.DataFrame([{
        
        'Married': 1 if married == "Yes" else 0,
        'Dependents': dependents,
        'Education': 1 if education == "Graduate" else 0,
        'Self_Employed': 1 if self_employed == "Yes" else 0,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history,
        'Property_Area': {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]
    }])
    prediction = model.predict(df)[0]
    if prediction == 1:
        st.success("✅ You are eligible for the loan!")
    else:
        st.error("❌ You are not eligible for the loan.")
