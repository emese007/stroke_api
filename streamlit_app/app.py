import streamlit as st 
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from streamlit_app import data

df = pd.read_parquet("../stroke_api/data/healthcare-dataset-stroke-data-clean.parquet")
'''
# Visualisation de données médicales d'une API

Bienvenue sur notre application médicale où vous pouvez obtenir les données des patients en temps et en heure 24h/24 7j/7 ! 
## Options : 
'''

stroke = st.segmented_control(
    "AVC?",
    ["Yes", "No", "Any"])
if stroke == "Yes":
    stroke = 1
elif stroke == "No":
    stroke = 0
elif stroke == "Any":
    stroke = None

genre = st.selectbox(
    'Genre',
     ["All", "Male", "Female", "Other"])

age = st.slider(label = "Age", min_value=0, max_value=100)

if st.checkbox('Show API call'):
    if genre == "All":
        genre = None
    data.API_call("http://127.0.0.1:8000/patients/", params={"gender":genre, "stroke":stroke, "max_age":age})
if genre == "All":
    genre = df["gender"]

if st.checkbox('Show DataFrame'):
    if stroke is None:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre)]
        st.dataframe(df_api)
    elif stroke is not None:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre) & (df["stroke"] == stroke)]
        st.dataframe(df_api)

option = st.multiselect(
    'Que voulez vous voir?',
     ["Age", "Taux d'AVC", "Genre"])

fig = make_subplots(rows=2, cols=2)

if "Age" in option:
    if stroke is None:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre)]
    else:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre) & (df["stroke"] == stroke)]
    fig.add_trace(
    go.Histogram(x=df_api["age"], name="Age"),
    row=1, col=1)


if "Genre" in option:
    if stroke is None:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre)]
    else:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre) & (df["stroke"] == stroke)]
    fig.add_trace(
    go.Histogram(x=df_api["gender"], name="Genre"),
    row=1, col=2)
    
if "Taux d'AVC" in option:
    if stroke is None:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre)]
    else:
        df_api = df[(df["age"] <= age) & (df["gender"] == genre) & (df["stroke"] == stroke)]
    fig.add_trace(
    go.Histogram(x=df_api["stroke"], name="Stroke"),
    row=2, col=1)

fig.update_layout(height=500, width=500)
st.plotly_chart(fig)

if stroke is None:
    df_api = df[(df["age"] <= age) & (df["gender"] == genre)]
else:
    df_api = df[(df["age"] <= age) & (df["gender"] == genre) & (df["stroke"] == stroke)]


col1, col2, col3 = st.columns(3)
col1.metric("Nombre total de patients", df_api["id"].count())
col2.metric("Âge moyen", round(df_api["age"].mean(), 1))
col3.metric("Taux d'AVC moyen", round(df_api["stroke"].mean(), 2))

dl_choice = st.sidebar.selectbox(
    "Save as",
    ("CSV", "JSON")
)

if stroke is None:
    if dl_choice == "CSV":
        to_dl = df[(df["age"] <= age) & (df["gender"] == genre)].to_csv()
    elif dl_choice == "JSON":
        to_dl = df[(df["age"] <= age) & (df["gender"] == genre)].to_json()
else:
    if dl_choice == "CSV":
        to_dl = df[(df["age"] <= age) & (df["gender"] == genre) & (df["stroke"] == stroke)].to_csv()
    elif dl_choice == "JSON":
        to_dl = df[(df["age"] <= age) & (df["gender"] == genre) & (df["stroke"] == stroke)].to_json()

st.sidebar.download_button(
    "Download", to_dl
)