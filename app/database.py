# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# 👇 Load variables from .env (like DATABASE_URL)
load_dotenv()

# 👇 Read the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# 👇 Creates connection with sql database
engine = create_engine(DATABASE_URL)

# 👇 Used to run querries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

