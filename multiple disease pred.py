# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:10:49 2023

@author: GHOST
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
 
diabetes_model = pickle.load(open('D:/ML-PROJECT/saved_3_models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('D:/ML-PROJECT/saved_3_models/heart_trained_model.sav', 'rb'))
breast_model = pickle.load(open('D:/ML-PROJECT/saved_3_models/breast_trained_model.sav', 'rb'))


with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System using ML',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Predicton',
                            'Breast Canser Prediction'],
                           
                           icons = ['activity', 'heart'],
                           
                          default_index = 0)
    
    
    
#diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    
        
        
    Pregnancies = st.text_input('number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin thickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
  
    #code for prdiction
    diab_diagnosis = ''
    
    # creating a button for Preduction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'the person is Diabetic'
            
        else:
            diab_diagnosis = 'the person is not Diabetic'
    st.success(diab_diagnosis)
  
#Heart Disease Predicton page
if (selected == 'Heart Disease Predicton'):
    
    #page title
    st.title('Heart Disease Predicton using ML')
    
    # age = st.text_input('age')
    # sex = st.text_input('sex')
    # cp = st.text_input('chest pain type (4 values)')
    # trestbps = st.text_input('resting blood pressure')
    # chol = st.text_input('serum cholestoral in mg/dl')
    # fbs = st.text_input('fasting blood sugar > 120 mg/dl')
    # restecg = st.text_input('resting electrocardiographic results (values 0,1,2)')
    # thalach = st.text_input('maximum heart rate achieved')
    # exang = st.text_input('exercise induced angina')
    # oldpeak = st.text_input('oldpeak = ST depression induced by exercise relative to rest')
    # slope = st.text_input('the slope of the peak exercise ST segment')
    # ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    # thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
   
  
    # #code for prdiction
    # heart_diagnosis = ''
    
    # # creating a button for Preduction
    
    # if st.button('heart didease Test Result'):
    #     heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
    #     if (heart_diagnosis[0]==1):
    #         heart_diagnosis = 'the person is Diabetic'
            
    #     else:
    #         heart_diagnosis = 'the person is not Diabetic'
    # st.success(heart_diagnosis)
    
    
#Breast Canser Prediction page
if (selected == 'Breast Canser Prediction'):
    
    #page title
    st.title('Breast Canser Prediction using ML')   
    
    # age = st.text_input('age')
    # sex = st.text_input('sex')
    # cp = st.text_input('chest pain type (4 values)')
    # trestbps = st.text_input('resting blood pressure')
    # chol = st.text_input('serum cholestoral in mg/dl')
    # fbs = st.text_input('fasting blood sugar > 120 mg/dl')
    # restecg = st.text_input('resting electrocardiographic results (values 0,1,2)')
    # thalach = st.text_input('maximum heart rate achieved')
    # exang = st.text_input('exercise induced angina')
    # oldpeak = st.text_input('oldpeak = ST depression induced by exercise relative to rest')
    # slope = st.text_input('the slope of the peak exercise ST segment')
    # ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    # thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
   
  
    # #code for prdiction
    # breast_diagnosis = ''
    
    # # creating a button for Preduction
    
    # if st.button('breast Test Result'):
    #     breast_prediction = breast_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
    #     if (breast_diagnosis[0]==1):
    #         breast_diagnosis = 'the person is '
            
    #     else:
    #         breast_diagnosis = 'the person is not '
    # st.success(breast_diagnosis)