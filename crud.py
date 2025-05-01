from sqlalchemy.orm import Session
from models import Patient, Admission, Doctor
from datetime import date

# Patients

def get_patients(db: Session):
    return db.query(Patient).all()

def create_patient(db: Session, first_name, last_name, gender, birth_date, city, province_id, allergies, height, weight):
    new_patient = Patient(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        birth_date=date.fromisoformat(birth_date),
        city=city,
        province_id=province_id,
        allergies=allergies,
        height=height,
        weight=weight
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def delete_patient(db: Session, patient_id: int):
    db.query(Patient).filter(Patient.patient_id == patient_id).delete()
    db.commit()

# Admissions

def get_admissions(db: Session):
    return db.query(Admission).all()

def create_admission(db: Session, patient_id, admission_date, discharge_date, diagnosis, attending_doctor_id):
    new_admission = Admission(
        patient_id=patient_id,
        admission_date=date.fromisoformat(admission_date),
        discharge_date=date.fromisoformat(discharge_date) if discharge_date else None,
        diagnosis=diagnosis,
        attending_doctor_id=attending_doctor_id
    )
    db.add(new_admission)
    db.commit()
    db.refresh(new_admission)
    return new_admission

def delete_admission(db: Session, patient_id: int):
    db.query(Admission).filter(Admission.patient_id == patient_id).delete()
    db.commit()

# Doctors

def get_doctors(db: Session):
    return db.query(Doctor).all()

def create_doctor(db: Session, first_name, last_name, specialty):
    new_doctor = Doctor(
        first_name=first_name,
        last_name=last_name,
        specialty=specialty
    )
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor

def delete_doctor(db: Session, doctor_id: int):
    db.query(Doctor).filter(Doctor.doctor_id == doctor_id).delete()
    db.commit()
