import streamlit as st
import joblib
import pandas as pd


model = joblib.load("notebooks/employee_attrition_model_reduced.joblib")

st.title("Employee Attrition Prediction")

st.write("Aplikasi untuk memprediksi seorang karyawan akan resign atau tidak")

st.success("Model berhasil dibuat")

with st.form("employee_form"):

    st.subheader("Employee Form")

    overtime = st.selectbox("Overtime", ["Yes", "No"])

    job_role = st.selectbox(
        "Job Role", 
        [
            "Sales Executive", 
            "Sales Representative",
            "Research Scientist",
            "Research Director",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Human Resources",
            "Manager"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

    business_travel = st.selectbox(
        "Business Travel",
        [
            "Non-Travel",
            "Travel_Rarely",
            "Travel_Frequently"
        ]
    )

    years_at_company = st.number_input(
        "Years At Company",
        min_value=0,
        step=1
    )

    years_current_role = st.number_input(
        "Years in current role",
        min_value=0,
        step=1
    )

    

        




