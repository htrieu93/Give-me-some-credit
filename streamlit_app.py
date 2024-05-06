import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load your model (if it's saved)
# model = joblib.load('credit_score_model.pkl')

# Assume the model is already in memory for this snippet
model = LinearRegression()
model.coef_ = np.array([0.285, 0.005])  # Assuming some coefficients
model.intercept_ = 200                 # Assuming an intercept

def predict_credit_score(age, income):
    input_data = np.array([[age, income]])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit user interface
st.title('Credit Score Prediction App')
st.write('This app predicts the credit score based on user input.')

age = st.slider('Age', 18, 65, 35)
income = st.number_input('Annual Income', min_value=30000, max_value=100000, value=50000)

if st.button('Predict Credit Score'):
    score = predict_credit_score(age, income)
    st.success(f'Predicted Credit Score: {score:.2f}')