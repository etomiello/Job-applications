from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() #this is for creating base class for all to inheir from

class Application(Base):
    #essentially need to make this so it matches my table i made in sql named applications 
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    application_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    last_update = Column(Date, nullable=False)
    resume_url = Column(String, nullable=True)
