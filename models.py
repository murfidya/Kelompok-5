from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from database import Base

class Patient(Base):
    __tablename__ = "patients"
    patient_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birth_date = Column(Date)
    city = Column(String)
    province_id = Column(Integer)
    allergies = Column(String)
    height = Column(Float)
    weight = Column(Float)

class Admission(Base):
    __tablename__ = "admissions"
    patient_id = Column(Integer, primary_key=True, index=True)
    admission_date = Column(Date)
    discharge_date = Column(Date, nullable=True)
    diagnosis = Column(String)
    attending_doctor_id = Column(Integer)

class Doctor(Base):
    __tablename__ = "doctors"
    doctor_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    specialty = Column(String)
