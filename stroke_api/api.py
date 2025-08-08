from fastapi import APIRouter
from stroke_api import filters
from enum import Enum

router = APIRouter()

class StatsName(str, Enum):
    number_stat = "nombre"
    age_moyen_stat = "age moyen"
    taux_avc_stat = "taux d'avc"
    all = "All"

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

@router.get("/patients/")
def get_patients(gender: str = None, stroke: int = None, max_age: float = None):
    filtered_df = filters.filter_patient(gender, stroke, max_age)
    return filtered_df

@router.get("/patients/{patient_id}")
def get_patients_id(patient_id:int):
    get_patient = filters.filter_id(patient_id)
    return get_patient


@router.get("/stats/{type}")
def get_stats(type: StatsName = None):
    result = filters.stats(type)
    return result
