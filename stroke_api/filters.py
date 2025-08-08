from typing import Optional
from fastapi import HTTPException
import plotly_express as px
import streamlit as st
import pandas as pd
from enum import Enum

# Chargement des données (une fois)

# Tester l'app avec :
# poetry run fastapi dev stroke_api/main.py
# http://127.0.0.1:8000/docs : utiliser la fonctionnalité Try it out pour tester les routes

# Ajout des fonctions de filtrage des données cf notebook 1
# Ensuite faire appel à ces fonctions dans le fichier api.py où sont définies les routes.

# Ajouter les fonctions de filtrage pour les autres routes.

stroke_data_df = pd.read_parquet("../stroke-api/data/healthcare-dataset-stroke-data-clean.parquet")

class StatsName(str, Enum):
    number_stat = "nombre"
    age_moyen_stat = "age moyen"
    taux_avc_stat = "taux d'avc"
    all = "All"

def filter_patient(gender:Optional[str] = None, stroke:Optional[bool] = None, max_age:Optional[float] = None):
    df = stroke_data_df.copy()

    if max_age is not None:
        df= df[df["age"] <= max_age]

    if gender is not None:
        df = df[df["gender"] == gender]

    if stroke is not None:
        df = df[df["stroke"] == stroke]

    return df.to_dict('records')

def read_patient(patient_id:int):
    return {"patient_id":patient_id}

def filter_id(id_patient:int):
    df = stroke_data_df.copy()
    
    if id_patient not in df["id"].tolist():
        raise HTTPException(status_code=404, detail="Patient not found")
    return df.loc[df["id"] == id_patient].to_dict('records')
    
def stats(type: StatsName = None):
# nb total de patients, âge moyen, taux d’AVC, répartition hommes/femmes
    df = stroke_data_df.copy()

    nb_patient = df["id"].count()
    age_moyen =  df["age"].mean()
    avc_moyen = df["stroke"].mean()
    
    if type == StatsName.number_stat:
        return {f"{round(nb_patient)} patients"}
    elif type == StatsName.age_moyen_stat:
        return {f"{round(age_moyen)} ans en moyenne"}
    elif type == StatsName.taux_avc_stat:
        return {f"{avc_moyen}% taux d'avc"}
    elif type == StatsName.all:
        return {f"{round(nb_patient)} patients, ", f"{round(age_moyen)} ans en moyenne, ", f"{avc_moyen}% taux d'avc"}
