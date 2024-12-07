# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:10:49 2023

@author: GHOST
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('D:/ML-PROJECT/saved_3_models/diabetes_trained_model.sav', 'rb'))
heart_model = pickle.load(open('D:/ML-PROJECT/saved_3_models/heart_trained_model.sav', 'rb'))
breast_model = pickle.load(open('D:/ML-PROJECT/saved_3_models/breast_trained_model.sav', 'rb'))


with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Predicton',
                            'Breast Canser Prediction'],
                          default_index = 0)
    
    
    
#diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
  
#Heart Disease Predicton page
if (selected == 'Heart Disease Predicton'):
    
    #page title
    st.title('Heart Disease Predicton using ML')
    
    
#Breast Canser Prediction page
if (selected == 'Breast Canser Prediction'):
    
    #page title
    st.title('Breast Canser Prediction using ML')   