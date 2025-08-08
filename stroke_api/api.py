from fastapi import APIRouter
from stroke_api import filters
from stroke_api.filters import filter_patient

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

@router.get("/patients/")
def get_patients(gender: str = None, stroke: int = None, max_age: float = None):
    result = filters.filter_patient(gender, stroke, max_age)
    return result

# TODO décommenter et compléter
@router.get("/patients/{patient_id}")
def get_patients_by_id(patient_id: int = None):
    result = filters.get_patients_by_id(patient_id)
    return result
    # Gérer le cas où l'id de patient passé en paramètre n'existe pas
    if patient_id.empty:
        
        raise HTTPException(404,"Patient ID not found")
        else:
        return patient.to_dict('records')

# TODO Ajout de la route stats
