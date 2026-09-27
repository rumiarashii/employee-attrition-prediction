import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

#cari model relatif terhadap lokasi app.py 
BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "models" / "employee_attrition_model_reduced.joblib")

st.title("Employee Attrition Prediction")

st.write("Aplikasi untuk memprediksi seorang karyawan akan resign atau tidak")

st.success("Model berhasil  dibuat")

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

    total_working_years = st.number_input(
        "Total Working Years",
        min_value = 0,
        step = 1
    )

    num_companies_worked = st.number_input(
        "Number of Companies Worked",
        min_value=0,
        step=1
    )

    years_current_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        step=1
    )

    environment_satisfaction = st.number_input(
        "Environment Satisfaction",
        min_value=1,
        max_value=4,
        step=1
    )

    job_satisfaction = st.number_input(
        "Job Satisfaction",
        min_value=1,
        max_value=4,
        step=1
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=0,
        step=1
    )

    job_level = st.number_input(
        "Job Level",
        min_value=1,
        max_value=5,
        step=1
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=0,
        step=100
    )

    years_since_promotion = st.number_input(
        "Years Since Last Promotion",
        min_value=0,
        step=1
    )

    submitted = st.form_submit_button("Submit")

    #ubah menjadi dict
    if submitted:
        input_data = {
            "OverTime": overtime,
            "JobRole": job_role,
            "YearsInCurrentRole": years_current_role,
            "MaritalStatus": marital_status,
            "YearsAtCompany": years_at_company,
            "TotalWorkingYears": total_working_years,
            "NumCompaniesWorked": num_companies_worked,
            "YearsWithCurrManager": years_current_manager,
            "EnvironmentSatisfaction": environment_satisfaction,
            "JobSatisfaction": job_satisfaction,
            "DistanceFromHome": distance_from_home,
            "JobLevel": job_level,
            "MonthlyIncome": monthly_income,
            "BusinessTravel": business_travel,
            "YearsSinceLastPromotion": years_since_promotion
        }

        input_df = pd.DataFrame([input_data])

        errors = []

        if years_current_role > years_at_company:
            errors.append("Years in Current Role cannot be bigger than Years At Company")

        if years_current_manager > years_at_company:
            errors.append("Years with Current Manager cannot be bigger than Years at Company")

        if years_at_company > total_working_years:
            errors.append("Years at company cannot be bigger than total working years")

        if years_since_promotion > years_at_company:
            errors.append("Years since promotion cannot be bigger than Years at Company")

        if errors:
            for error in errors:
                st.error(error)
        else:
            st.subheader("Input Data")
            st.dataframe(input_df)
            
            prediction = model.predict(input_df)[0]
            probability_yes = model.predict_proba(input_df)[0,1]
            
            result = "Yes" if prediction == 1 else "No"
            
            st.subheader("Prediction Result")
            
            if prediction == 1:
                st.warning(f"Attrition Prediction: {result}")
            else:
                st.success(f"Attrition Prediction: {result}")
            
                st.metric("Probability of Attrition", f"{probability_yes:.2%}")

        






    



        




