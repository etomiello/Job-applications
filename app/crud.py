from sqlalchemy.orm import Session
from app import models

def create_application(db: Session, application_data):
    new_application = models.Application(**application_data.dict())  #modkes.application Uses that dictionary to create a new SQLAlchemy model instanc------application_data Converts the Pydantic model (ApplicationCreate) to a dictionary
    db.add(new_application) #Adds the object to the current DB session
    db.commit() #Executes the actual SQL INSERT
    db.refresh(new_application)  # Fetch the newly created row (with ID)
    return new_application #sends back new record

def get_all_applications(db: Session):
    return db.query(models.Application).all()

def get_application_by_id(db: Session, application_id: int):
    return db.query(models.Application).filter(models.Application.id == application_id).first()

def update_application(db: Session, application_id: int, application_data):
    application = db.query(models.Application).filter(models.Application.id == application_id).first()
    if not application:
        return None  # Or raise HTTPException inside route
    for key, value in application_data.dict().items():
        setattr(application, key, value)

    db.commit()
    db.refresh(application)
    return application