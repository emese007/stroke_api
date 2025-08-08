import streamlit as st 
import pandas as pd
import requests
from streamlit_app import data
from streamlit_app import home
from streamlit_app import stats
from streamlit_app import graphs

'''
# Visualisation de données médicales d'une API

Bienvenue sur notre application médicale où vous pouvez obtenir les meilleures stats en temps et en heure 24h/24 7j/7.
'''
if st.checkbox('Show API call'):
    API_data = data.API_call("http://127.0.0.1:8000/patients/", params={"gender":"Male"})

    API_data

option = st.selectbox(
    'Que voulez vous voir?',
     ["Age", "Taux d'AVC", "Genre"])