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

def categorize_age(age):
    if age <= 10:
        return 1
    elif age <= 20:
        return 2
    elif age <= 30:
        return 3
    elif age <= 40:
        return 4
    elif age <= 50:
        return 5
    elif age <= 60:
        return 6
    elif age <= 70:
        return 7
    elif age <= 80:
        return 8
    elif age <= 90:
        return 9
    else:
        return 10

def main():
    st.set_page_config(page_title='Diabetes Readmission Prediction', layout='wide')
    
    st.title('🏥 Early Readmission Prediction for Diabetic Patients')
    st.markdown('This application predicts whether a diabetic patient is at high risk of early hospital readmission, helping healthcare providers make informed decisions.')
    
    col1, col2 = st.columns([1, 1])
    
    with col2:
        st.markdown('### 📢 Importance of Early Readmission Prediction')
        st.markdown('Predicting early readmission is crucial in improving patient outcomes and reducing healthcare costs. By identifying high-risk patients, hospitals can implement preventive measures, offer tailored post-discharge plans, and enhance overall efficiency.')
        
        st.markdown('Early hospital readmission can indicate gaps in post-discharge care and patient monitoring. By leveraging data-driven predictions, healthcare systems can improve patient management strategies, reduce unnecessary re-hospitalizations, and ensure continuity of care. Effective prediction models assist in better resource allocation, reducing patient burden and financial strain on both hospitals and individuals.')
        
        # Load and resize hospital image
        hospital_image = Image.open('hospital.png').resize((800, 500))
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
        gender = st.radio('Select Gender:', ['Male', 'Female'])
        gender_value = 0 if gender == 'Male' else 1
        
        age = int(st.number_input('Enter Age:', min_value=0, max_value=120))
        age_category = categorize_age(age)
        
        admission_type_id = int(st.selectbox('Admission Type (1 - Emergency, 2 - Urgent, etc.)', [1, 2, 3, 4, 5, 6, 7, 8]))
        time_in_hospital = int(st.number_input('Time in Hospital (Days)', min_value=1, max_value=30))
        num_lab_procedures = int(st.number_input('Number of Lab Procedures', min_value=0))
        num_medications = int(st.number_input('Number of Medications', min_value=0))
        number_inpatient = int(st.number_input('Number of Inpatient Visits', min_value=0))
        diag_1 = int(st.number_input('Primary Diagnosis Code'))
        diag_2 = int(st.number_input('Secondary Diagnosis Code'))
        diag_3 = int(st.number_input('Additional Diagnosis Code'))
        metformin = int(st.selectbox('Metformin Use (0 - No, 1 - Yes)', [0, 1]))
        insulin = int(st.selectbox('Insulin Use (1 - No, 2 - Up, 3 - Steady)', [1, 2, 3]))
        change = int(st.selectbox('Change in Medications (0 - No, 1 - Yes)', [0, 1]))
        diabetesMed = int(st.selectbox('Diabetes Medication (0 - No, 1 - Yes)', [0, 1]))
        discharged_to = int(st.number_input('Discharge Destination Code', min_value=1, max_value=30))
        
        input_list = [[gender_value, age_category, admission_type_id, time_in_hospital, num_lab_procedures,
                       num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                       insulin, change, diabetesMed, discharged_to]]
        
        st.markdown("### 🏥 Prediction")
        if st.button('🚀 Predict', use_container_width=True):
            with st.spinner('Processing...'):
                response = prediction(input_list)
                st.success(f'🔍 Prediction Result: **{response}**')
    
if __name__ == '__main__':
    main()
