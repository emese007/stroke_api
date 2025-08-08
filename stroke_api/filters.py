#from typing import Optional
import pandas as pd

# Chargement des données (une fois)
stroke_data_df = pd.read_parquet("../stroke-api/data/healthcare-dataset-stroke-data-clean.parquet")

# Tester l'app avec :
#poetry run fastapi dev stroke_api/main.py
# http://127.0.0.1:8000/docs : utiliser la fonctionnalité Try it out pour tester les routes

# Ajout des fonctions de filtrage des données cf notebook 1

def filter_patient(gender: str = None, stroke: int = None, max_age: float = None):

    filter_df = stroke_data_df.copy()

    if gender is not None:
        filter_df = filter_df[filter_df['gender'] == gender]

    if stroke is not None:
        filter_df = filter_df[filter_df['stroke'] == stroke]

    if max_age is not None:
        filter_df = filter_df[filter_df['age'] <= max_age]

    return filter_df.to_dict('records')

# Ensuite faire appel à ces fonctions dans le fichier api.py où sont définies les routes.

# Ajouter les fonctions de filtrage pour les autres routes.

def get_patients_by_id(patient_id: int = None):
    
    filter_df = stroke_data_df.copy()

    patient = filter_df.loc[filter_df["id"] == patient_id]

    if patient.empty:
        return None

    return patient.to_dict('records')


