import streamlit as st
from streamlit_app import patients
from streamlit_app import graphs
from streamlit_app import home

st.set_page_config(
    page_title="Handy Stroke Candy",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

if "page" not in st.session_state:
    st.session_state.page = "Accueil"

def go(page_name: str):
    st.session_state.page = page_name

with st.sidebar:
    st.title("Navigation")
    st.button("Accueil", on_click=go, args=("Accueil",))
    st.button("Données des patients", on_click=go, args=("Patient_id",))
    st.button("Visualisations", on_click=go, args=("Visualisations",))

page = st.session_state.page
if page == "Accueil":
    home.page_accueil()
elif page == "Patient_id":
    patients.page_patient()
elif page == "Visualisations":
    graphs.page_graphs()
else:
    st.warning("Page inconnue, retour à l’accueil.")
    go("Accueil")