import streamlit as st
import plotly.express as px
import pandas as pd
import requests

def API_call_patient_data(age, genre, stroke):
    url = "http://127.0.0.1:8000/patients/" 
    params={"gender":genre, "stroke":stroke, "max_age":age}
    data = requests.get(url, params).json()
    return data

def API_call_patient_id(patient_id):
        url = f"http://127.0.0.1:8000/patients/{patient_id}" 
        data = requests.get(url).json()
        return data

def API_call_patient_stats(type):
        url = f"http://127.0.0.1:8000/stats/{type}" 
        data = requests.get(url).json()
        return data[0]