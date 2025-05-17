import streamlit as st
import pandas as pd
import joblib

# Load models
linreg_model = joblib.load("models/MP3ML.pkl")
meanshift_model = joblib.load("models/meanshift_model.pkl")
kmeans_model = joblib.load("models/kmeans_model.pkl")

st.title("Employee Behavior Prediction")

# Select model
model_choice = st.selectbox("Select a model:", ["Linear Regression", "MeanShift", "K-Means Clustering"])

# Input section
st.subheader("Enter employee data:")

job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
jobrole = st.selectbox("Job Role", list(range(9)))  # 0–8
department = st.selectbox("Department", [0, 1, 2])
education = st.selectbox("Education", [1, 2, 3, 4, 5])
education_field = st.selectbox("Education Field", list(range(6)))  # 0–5
totalworkingyears = st.slider("Total Working Years", min_value=0, max_value=40, value=10)


# Build input data
input_data = pd.DataFrame([[
    job_level, jobrole, department, education, education_field, totalworkingyears
]], columns=[
    "JobLevel", "Job Role", "Department", "Education", "Education Field", "Total Working Years"
])

# Predict
if st.button("Predict"):
    if model_choice == "Linear Regression":
        prediction = linreg_model.predict(input_data)
        st.write(f"Predicted monthly income: {round(prediction[0][0], 2)} DKK")

    elif model_choice == "MeanShift":
        label = meanshift_model.predict(input_data)[0]
        st.write(f"Cluster assignment: {label}")

    elif model_choice == "K-Means Clustering":
        label = kmeans_model.predict(input_data)[0]
        st.write(f"Cluster assignment: {label}")
