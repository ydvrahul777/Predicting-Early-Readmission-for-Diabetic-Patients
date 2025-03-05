
import streamlit as st
import numpy as np
import pandas as pd
import pickle 

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
    st.title('Early Readmission Prediction for Diabetic Patients')
    st.subheader('This application predicts whether a diabetic patient is at high risk of early hospital readmission.')
    
    st.markdown('### Input Patient Data')
    st.markdown('Please enter the following details to get a prediction:')
    
    gender = st.selectbox('Gender', [0.0, 1.0], help='0: Male, 1: Female')
    age = st.number_input('Age Group', min_value=1.0, max_value=10.0, help='Categorized age group (1: 0-10, 2: 10-20, etc.)')
    admission_type_id = st.selectbox('Admission Type', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], help='Type of admission (e.g., emergency, elective, urgent)')
    time_in_hospital = st.number_input('Time in Hospital (Days)', min_value=1.0, max_value=30.0, help='Number of days the patient stayed in the hospital')
    num_lab_procedures = st.number_input('Number of Lab Procedures', min_value=0.0, help='Total number of lab tests performed')
    num_medications = st.number_input('Number of Medications', min_value=0.0, help='Total number of medications prescribed')
    number_inpatient = st.number_input('Number of Inpatient Visits', min_value=0.0, help='Previous inpatient visits')
    diag_1 = st.number_input('Primary Diagnosis Code', help='ICD-9 numerical code for the primary diagnosis')
    diag_2 = st.number_input('Secondary Diagnosis Code', help='ICD-9 numerical code for the secondary diagnosis')
    diag_3 = st.number_input('Additional Diagnosis Code', help='ICD-9 numerical code for any additional diagnosis')
    metformin = st.selectbox('Metformin Use', [0.0, 1.0], help='0: No, 1: Yes')
    insulin = st.selectbox('Insulin Use', [1.0, 2.0, 3.0], help='1: No, 2: Up, 3: Steady')
    change = st.selectbox('Change in Medications', [0.0, 1.0], help='0: No, 1: Yes')
    diabetesMed = st.selectbox('Diabetes Medication', [0.0, 1.0], help='0: No, 1: Yes')
    discharged_to = st.number_input('Discharge Destination Code', min_value=1.0, max_value=30.0, help='Numerical code representing discharge destination')
    
    input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]
    
    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()
