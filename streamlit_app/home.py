import streamlit as st
from streamlit_app import data

def page_accueil():
    st.title("Stroke Dataset Explorer")
    st.subheader("Objectifs de l'application")
    st.markdown(
        "Cette application a pour objectif d’explorer interactivement un jeu de données santé "
        "(prédiction d’AVC) et de montrer comment un backend FastAPI peut être consommé par une "
        "interface Streamlit."
    )
    st.markdown(
        "- Filtrer la liste des patients (genre, AVC 0/1, âge max).\n"
        "- Consulter des statistiques clés : nombre total de patients, âge moyen, taux d’AVC, "
        "répartition hommes/femmes.\n"
        "- Visualiser rapidement ces informations sous forme de graphiques.\n"
    )

    st.subheader("Quelque statistiques")
    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre total de patients", data.API_call_patient_stats("nombre"))
    col2.metric("Âge moyen", data.API_call_patient_stats("age moyen"))
    col3.metric("Taux d'AVC moyen", data.API_call_patient_stats("taux d'avc"))