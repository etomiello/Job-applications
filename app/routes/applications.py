from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, crud
from datetime import date


router = APIRouter()

# Dependency to get DB session
def get_db():   #This is FastAPI’s recommended pattern for managing DB sessions.
    db = SessionLocal() #Starts a new session with the DB (i.e., opens a connection to RDS)
    try:
        yield db #gives the calling function access to the db object temporarily.
    finally:
        db.close() 

# Request model for creating a new application
class ApplicationCreate(BaseModel):
    company_name: str
    job_title: str
    application_date: date
    status: str
    last_update: date      
    resume_url: Optional[str] = None


class ApplicationOut(BaseModel):
    id: int
    company_name: str
    job_title: str
    application_date: date
    status: str
    last_update: date
    resume_url: Optional[str] = None

    class Config:
        from_attributes = True  # For Pydantic v2, replaces orm_mode



@router.post("/applications", response_model=ApplicationOut) #@router Defines a new POST route at /applications---- response_model Automatically formats the response using ApplicationOut (adds id, hides internal fields)
def create_application_route(application: ApplicationCreate, db: Session = Depends(get_db)): #FastAPI will run this function when the route is called--- application create, FastAPI will parse the request body using this Pydantic model -- db Injects a SQLAlchemy DB session using your helper function 
    return crud.create_application(db, application) #Calls the logic you wrote in crud.py and returns the result
