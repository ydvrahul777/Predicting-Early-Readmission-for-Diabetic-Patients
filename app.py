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
    st.markdown('This application predicts whether a diabetic patient is at high risk of early hospital readmission, helping healthcare providers make informed decisions.')
    
    col1, col2 = st.columns([1, 1])
    
    with col2:
        # Load and resize hospital image
        hospital_image = Image.open('hospital.png').resize((600, 400))
        st.image(hospital_image, caption='Hospital Readmission Prediction')
        
        
        st.markdown('---')
        st.markdown('### 📢 How This Helps')
        st.markdown('**For Patients:** This model helps in identifying individuals who are at higher risk of early readmission, ensuring timely interventions and better healthcare management.')
        st.markdown('**For Hospitals:** By predicting readmissions, hospitals can optimize resource allocation, improve patient care, and reduce unnecessary hospital stays, ultimately enhancing efficiency and cost savings.')
        
        st.markdown('---')
        st.markdown('### 📢 About this App')
        st.markdown('This app is designed to assist healthcare providers in identifying diabetic patients at risk of early readmission. The prediction is based on patient demographics, medical history, and admission details.')
    
    with col1:
        st.header('Patient Information')
        gender = st.selectbox('Gender (0 - Male, 1 - Female)', [0.0, 1.0])
        age = st.number_input('Age Group (1: 0-10, ..., 10: 90-100)', min_value=1.0, max_value=10.0)
        admission_type_id = st.selectbox('Admission Type (1 - Emergency, 2 - Urgent, etc.)', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        time_in_hospital = st.number_input('Time in Hospital (Days)', min_value=1.0, max_value=30.0)
        num_lab_procedures = st.number_input('Number of Lab Procedures', min_value=0.0)
        num_medications = st.number_input('Number of Medications', min_value=0.0)
        number_inpatient = st.number_input('Number of Inpatient Visits', min_value=0.0)
        diag_1 = st.number_input('Primary Diagnosis Code')
        diag_2 = st.number_input('Secondary Diagnosis Code')
        diag_3 = st.number_input('Additional Diagnosis Code')
        metformin = st.selectbox('Metformin Use (0 - No, 1 - Yes)', [0.0, 1.0])
        insulin = st.selectbox('Insulin Use (1 - No, 2 - Up, 3 - Steady)', [1.0, 2.0, 3.0])
        change = st.selectbox('Change in Medications (0 - No, 1 - Yes)', [0.0, 1.0])
        diabetesMed = st.selectbox('Diabetes Medication (0 - No, 1 - Yes)', [0.0, 1.0])
        discharged_to = st.number_input('Discharge Destination Code', min_value=1.0, max_value=30.0)
        
        input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                       num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                       insulin, change, diabetesMed, discharged_to]]
        
        st.markdown("### 🏥 Prediction")
        if st.button('🚀 Predict', use_container_width=True):
            with st.spinner('Processing...'):
                response = prediction(input_list)
                st.success(f'🔍 Prediction Result: **{response}**')
    
if __name__ == '__main__':
    main()
