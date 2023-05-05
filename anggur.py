import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('prediksi_wine.sav', 'rb'))

# judul web
st.title('Prediksi Kualitas Anggur')
st.text('Yulinawati - 201351139 - Malam A')

acidity = st.number_input('Fixed Acidity')

volatile = st.number_input('volatile Acidity')

citric = st.number_input('Citric Acid')

residual = st.number_input('Residual Sugar')

chlorides = st.number_input('Chlorides')

FSD = st.number_input('Free Sulfur Dioxide')

TSD = st.number_input('Total Sulfur Dioxide')

density = st.number_input('Density')

pH = st.number_input('pH')

sulphates = st.number_input('Sulphates')

alcohol = st.number_input('Alcohol')

# code for prediction
Kualitas_Anggur = ''

if st.button ('Prediksi Kualitas Anggur') :
    Kualitas_Anggur = model.predict([[acidity, volatile, citric, residual, chlorides, FSD, TSD, density, pH, sulphates, alcohol]])
    
    if (Kualitas_Anggur[0]==1):
        Kualitas_Anggur = 'Kualitas Anggur Buruk'
    else:
        Kualitas_Anggur = 'Kualitas Anggur Baik'
        
st.success(Kualitas_Anggur)
