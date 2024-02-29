from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
# Connection details
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine and session maker
engine = create_engine(DATABASE_URL)
SessionLocalBase = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency to get a database session
def get_db():
    db = SessionLocalBase()
    try:
        yield db
    finally:
        db.close()
