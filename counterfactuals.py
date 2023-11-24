import streamlit as st
import pandas as pd
import datetime
import os
import bcrypt
from hashlib import sha256
from io import StringIO

# Main app
def main_app():
    # Display an image
    image_path = '/Users/jedalvin/projecthome_cover.png'
    st.image(image_path)
    st.markdown("Objective: ")
    
    st.title('Home Purchase Prediction')
