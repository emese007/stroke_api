import streamlit as st
import plotly.express as px
import pandas as pd

frame = pd.read_parquet("../stroke_api/data/healthcare-dataset-stroke-data-clean.parquet")

def page_graphs():
    st.title("Visualisations")
    col1, col2, col3 = st.columns(3)
    with col1:
        stroke = st.segmented_control(
            "AVC?",
            ["Yes", "No", "Any"])
        if stroke == "Yes":
            stroke = 1
        elif stroke == "No":
            stroke = 0
        elif stroke == "Any":
            stroke = None
    with col2:
        genre = st.selectbox(
            'Genre',
            ["All", "Male", "Female", "Other"])
    with col3:
        age = st.slider(label = "Age", min_value=0, max_value=100)
    graphs_display(age, genre, stroke)


def graphs_display(val1, val2, val3):

    tab1, tab2, tab3 = st.tabs(["Âge", "Genre", "Stroke"])

    if val2 == "All":
        val2 = frame["gender"]
    if val3 is None:
        val3 = frame["stroke"]

    with tab1:
        frame_api = frame[(frame["age"] <= val1) & (frame["gender"] == val2) & (frame["stroke"] == val3)]
        fig1 = px.histogram(frame_api, x=["age"], title="Distribution de l'âge", labels={"value":"Âge"})
        fig1.update_layout(yaxis_title="Nombre d'individus")
        st.plotly_chart(fig1, key="age_histogram")

    with tab2:
        frame_api = frame[(frame["age"] <= val1) & (frame["gender"] == val2) & (frame["stroke"] == val3)]
        fig2 = px.histogram(frame_api, x=["gender"], title="Distribution des genres", labels={"value":"Genres"})
        fig2.update_layout(yaxis_title="Nombre d'individus")
        st.plotly_chart(fig2, key="gender_histogram")

    with tab3:
        frame_api = frame[(frame["age"] <= val1) & (frame["gender"] == val2) & (frame["stroke"] == val3)]
        fig3 = px.histogram(frame_api, x=["stroke"], title="Taux d'AVC", labels={"value":"AVC"})
        fig3.update_layout(yaxis_title="Nombre d'individus")
        st.plotly_chart(fig3, key="stroke_histogram")
