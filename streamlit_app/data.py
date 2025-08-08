import streamlit as st 
import pandas as pd
import requests

def API_call():
    data = requests.get("http://127.0.0.1:8000/patients/").json()

    st.write(data)

