import streamlit as st
import pandas as pd
import datetime
import os
import bcrypt
from hashlib import sha256
from io import StringIO

# Your pre-trained model
model = load_model('pipeline.joblib')

st.title('Home Purchase Prediction')

# Display the cover image
st.image('projecthome_cover.PNG', caption='Home Purchase Predictor')

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('Data Preview:', data.head())

# Run the app
if __name__ == '__main__':
    st.run()
