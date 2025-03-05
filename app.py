import streamlit as st
import numpy as np
import pandas as pd
import pickle 
from PIL import Image

# Load the trained model
with open('final_model.pkl','rb') as file:
    model = pickle.load(file)

def prediction(input_data):
    pred = model.predict(input_data)[0]
    
    if pred == 1:
        return 'High Risk of Readmission'
    else:
        return 'Low Risk of Readmission'

def main():
    st.set_page_config(page_title='Diabetes Readmission Prediction', layout='wide')
    
    st.title('🏥 Early Readmission Prediction for Diabetic Patients')
    st.markdown('This application predicts whether a diabetic patient is at high risk of early hospital readmission.')
    
    # Load and resize hospital image
    hospital_image = Image.open('hospital.png').resize((600, 350))
    st.image(hospital_image, caption='Hospital Readmission Prediction')
    
    st.sidebar.header('Patient Information')
    
    gender = st.sidebar.selectbox('Gender (0 - Male, 1 - Female)', [0.0, 1.0])
    age = st.sidebar.number_input('Age Group (1: 0-10, ..., 10: 90-100)', min_value=1.0, max_value=10.0)
    admission_type_id = st.sidebar.selectbox('Admission Type (1 - Emergency, 2 - Urgent, etc.)', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    time_in_hospital = st.sidebar.number_input('Time in Hospital (Days)', min_value=1.0, max_value=30.0)
    num_lab_procedures = st.sidebar.number_input('Number of Lab Procedures', min_value=0.0)
    num_medications = st.sidebar.number_input('Number of Medications', min_value=0.0)
    number_inpatient = st.sidebar.number_input('Number of Inpatient Visits', min_value=0.0)
    diag_1 = st.sidebar.number_input('Primary Diagnosis Code')
    diag_2 = st.sidebar.number_input('Secondary Diagnosis Code')
    diag_3 = st.sidebar.number_input('Additional Diagnosis Code')
    metformin = st.sidebar.selectbox('Metformin Use (0 - No, 1 - Yes)', [0.0, 1.0])
    insulin = st.sidebar.selectbox('Insulin Use (1 - No, 2 - Up, 3 - Steady)', [1.0, 2.0, 3.0])
    change = st.sidebar.selectbox('Change in Medications (0 - No, 1 - Yes)', [0.0, 1.0])
    diabetesMed = st.sidebar.selectbox('Diabetes Medication (0 - No, 1 - Yes)', [0.0, 1.0])
    discharged_to = st.sidebar.number_input('Discharge Destination Code', min_value=1.0, max_value=30.0)
    
    
    input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]
    
    if st.button('🚀 Predict'):
        with st.spinner('Processing...'):
            response = prediction(input_list)
            st.success(f'🔍 Prediction Result: **{response}**')
    
    st.markdown('---')
    st.markdown('### 📢 About this App')
    st.markdown('This app is designed to assist healthcare providers in identifying diabetic patients at risk of early readmission. The prediction is based on patient demographics, medical history, and admission details.')
    
if __name__ == '__main__':
    main()
