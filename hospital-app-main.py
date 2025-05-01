from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Patients routes
@app.get("/patients")
def list_patients(request: Request, db: Session = Depends(get_db)):
    patients = crud.get_patients(db)
    return templates.TemplateResponse("patients.html", {"request": request, "patients": patients})

@app.post("/patients/create")
def create_patient(
    first_name: str = Form(...),
    last_name: str = Form(...),
    gender: str = Form(...),
    birth_date: str = Form(...),
    city: str = Form(...),
    province_id: int = Form(...),
    allergies: str = Form(...),
    height: float = Form(...),
    weight: float = Form(...),
    db: Session = Depends(get_db)):
    crud.create_patient(db, first_name, last_name, gender, birth_date, city, province_id, allergies, height, weight)
    return RedirectResponse(url="/patients", status_code=303)

@app.post("/patients/delete/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    crud.delete_patient(db, patient_id)
    return RedirectResponse(url="/patients", status_code=303)

# Repeat similar for admissions and doctors
@app.get("/admissions")
def list_admissions(request: Request, db: Session = Depends(get_db)):
    admissions = crud.get_admissions(db)
    return templates.TemplateResponse("admissions.html", {"request": request, "admissions": admissions})

@app.post("/admissions/create")
def create_admission(
    patient_id: int = Form(...),
    admission_date: str = Form(...),
    discharge_date: str = Form(None),
    diagnosis: str = Form(None),
    attending_doctor_id: int = Form(None),
    db: Session = Depends(get_db)):
    crud.create_admission(db, patient_id, admission_date, discharge_date, diagnosis, attending_doctor_id)
    return RedirectResponse(url="/admissions", status_code=303)

@app.post("/admissions/delete/{patient_id}")
def delete_admission(patient_id: int, db: Session = Depends(get_db)):
    crud.delete_admission(db, patient_id)
    return RedirectResponse(url="/admissions", status_code=303)

@app.get("/doctors")
def list_doctors(request: Request, db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db)
    return templates.TemplateResponse("doctors.html", {"request": request, "doctors": doctors})

@app.post("/doctors/create")
def create_doctor(
    first_name: str = Form(...),
    last_name: str = Form(...),
    specialty: str = Form(...),
    db: Session = Depends(get_db)):
    crud.create_doctor(db, first_name, last_name, specialty)
    return RedirectResponse(url="/doctors", status_code=303)

@app.post("/doctors/delete/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    crud.delete_doctor(db, doctor_id)
    return RedirectResponse(url="/doctors", status_code=303)
