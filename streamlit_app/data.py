import streamlit as st 
import pandas as pd
import requests

def API_call(url, params):
    data = requests.get(url, params).json()

    return st.write(data)