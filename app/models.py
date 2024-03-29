from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for models
Base = declarative_base()


class ShortenedUrl(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True)
    original_url = Column(String(255), unique=True)
    short_link = Column(String(7), unique=True, index=True)
