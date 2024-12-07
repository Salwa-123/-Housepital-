# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:55:16 2023

@author: GHOST
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/ML-PROJECT/diabetes_content/diabetes_trained_model.sav' , 'rb'))

#creating a function of prediction

def diapetes_prediction(input_data):
    
   

    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')

                           
      
      

def main():
    #giving a title
    st.title('Diapetes prediction web App')
    
    #getting the input data from the user
    
    
    Pregnancies = st.text_input('number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin thickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    
    #code for prdiction
    diagnosis = ''
    
    # creating a button for Preduction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diapetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    
    st.success(diagnosis)
    
    
    
    
    
    
if __name__ == '__main__':
    main()