import streamlit as st
import pickle
import pandas as pd

# App Header
st.header('Advertising Revenue Forecaster')
st.subheader('Estimate the impact of your marketing budget on sales performance.')

# Load the pre-trained model
with open('modeladvertising.pkl', 'rb') as model_file:
    sales_model = pickle.load(model_file)

# Input Section
st.markdown('**Input your advertising expenses below (in $1,000s):**')
tv_budget = st.number_input('TV Budget')
radio_budget = st.number_input('Radio Budget')
newspaper_budget = st.number_input('Newspaper Budget')

# Prepare input data for prediction
budget_data = pd.DataFrame({
    'TV': [tv_budget],
    'Radio': [radio_budget],
    'Newspaper': [newspaper_budget]
})

# Prediction Logic
if st.button('Estimate Sales'):
    predicted_sales = sales_model.predict(budget_data)
    result = f"Estimated Sales Revenue: ${predicted_sales[0]:,.2f}"
    st.success(result)

# Footer
st.caption('Optimize your marketing strategy with data-driven insights!')