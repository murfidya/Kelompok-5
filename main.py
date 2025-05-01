from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
from database import SessionLocal, engine
from models import Base
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return RedirectResponse(url="/patients")

@app.get("/patients")
def list_patients(request: Request):
    db = next(get_db())
    patients = crud.get_patients(db)
    return templates.TemplateResponse("patients.html", {"request": request, "patients": patients})

@app.post("/patients/create")
def create_patient(
    first_name: str = Form(...), last_name: str = Form(...), gender: str = Form(...),
    birth_date: str = Form(...), city: str = Form(...), province_id: int = Form(...),
    allergies: str = Form(...), height: float = Form(...), weight: float = Form(...)):
    db = next(get_db())
    crud.create_patient(db, first_name, last_name, gender, birth_date, city, province_id, allergies, height, weight)
    return RedirectResponse(url="/patients", status_code=HTTP_303_SEE_OTHER)

@app.post("/patients/delete/{patient_id}")
def delete_patient(patient_id: int):
    db = next(get_db())
    crud.delete_patient(db, patient_id)
    return RedirectResponse(url="/patients", status_code=HTTP_303_SEE_OTHER)

@app.get("/admissions")
def list_admissions(request: Request):
    db = next(get_db())
    admissions = crud.get_admissions(db)
    return templates.TemplateResponse("admissions.html", {"request": request, "admissions": admissions})

@app.post("/admissions/create")
def create_admission(
    patient_id: int = Form(...), admission_date: str = Form(...), discharge_date: str = Form(None),
    diagnosis: str = Form(...), attending_doctor_id: int = Form(...)):
    db = next(get_db())
    crud.create_admission(db, patient_id, admission_date, discharge_date, diagnosis, attending_doctor_id)
    return RedirectResponse(url="/admissions", status_code=HTTP_303_SEE_OTHER)

@app.post("/admissions/delete/{patient_id}")
def delete_admission(patient_id: int):
    db = next(get_db())
    crud.delete_admission(db, patient_id)
    return RedirectResponse(url="/admissions", status_code=HTTP_303_SEE_OTHER)

@app.get("/doctors")
def list_doctors(request: Request):
    db = next(get_db())
    doctors = crud.get_doctors(db)
    return templates.TemplateResponse("doctors.html", {"request": request, "doctors": doctors})

@app.post("/doctors/create")
def create_doctor(first_name: str = Form(...), last_name: str = Form(...), specialty: str = Form(...)):
    db = next(get_db())
    crud.create_doctor(db, first_name, last_name, specialty)
    return RedirectResponse(url="/doctors", status_code=HTTP_303_SEE_OTHER)

@app.post("/doctors/delete/{doctor_id}")
def delete_doctor(doctor_id: int):
    db = next(get_db())
    crud.delete_doctor(db, doctor_id)
    return RedirectResponse(url="/doctors", status_code=HTTP_303_SEE_OTHER)
