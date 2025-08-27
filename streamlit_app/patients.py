import streamlit as st
import pandas as pd
from streamlit_app import data

def page_patient():
    
    df2 = pd.DataFrame()
    st.title("Données des patients")

    patient_id = st.text_input(label="Patient ID", placeholder="Ici, tapes l'ID existant d'un patient.")

    if "patient_id_df" not in st.session_state:
        st.session_state.patient_id_df = None

    if st.button(label="Search patient"):
        if data.API_call_patient_id(patient_id) == {"detail":"Patient not found"}:
            st.write("Patient ID does not exist!")
            st.session_state.patient_id_df = None
        else:
            st.session_state.patient_id_df = pd.DataFrame(data.API_call_patient_id(patient_id))
    if st.session_state.patient_id_df is not None:
        st.dataframe(st.session_state.patient_id_df)

    col1, col2, col3 = st.columns(3)
    
    if "patient_df" not in st.session_state:
        st.session_state.patient_df = None

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
    if st.button(label="Search"):
        if genre == "All":
            genre = None
        st.session_state.patient_df = pd.DataFrame(data.API_call_patient_data(age, genre, stroke))
    if st.session_state.patient_df is not None:
        st.dataframe(st.session_state.patient_df)