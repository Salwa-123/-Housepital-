# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 05:38:39 2023

@author: GHOST
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/ML-PROJECT/heart_disease_content/heart_trained_model.sav' , 'rb'))



#creating a function of prediction

def heart_disease_prediction(input_data):
    
    
        # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)
    
    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0]== 0):
      print('The Person does not have a Heart Disease')
    else:
      print('The Person has Heart Disease')
      
      

def main():
    #giving a title
    st.title('Heart Disease prediction web App')
    
    #getting the input data from the user
    
    
    age = st.text_input('number of Pregnancies')
    sex = st.text_input('Glucose level')
    cp = st.text_input('Blood Pressure value')
    trestbps = st.text_input('Skin thickness value')
    chol = st.text_input('Insulin level')
    fbs = st.text_input('BMI value')
    restecg = st.text_input('Diabetes Pedigree Function value')
    thalach = st.text_input('Age of the person')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('tha1')
    
    
    #code for prdiction
    heart_diagnosis = ''
    
    # creating a button for Preduction
    
    if st.button('Heaert Disease Test Result'):
        heart_diagnosis = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        if (heart_diagnosis[0]== 1):
          heart_diagnosis = 'The Person does not have a Heart Disease'
        else:
          heart_diagnosis = 'The Person has Heart Disease'
    
    st.success(heart_diagnosis)
    
    
    
    
    
    
#if __name__ == '__main__':
    main()      