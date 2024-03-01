from fastapi import FastAPI, Depends, HTTPException
from schemas import ShortenedUrlCreate, ShortenedUrlResponse
from sqlalchemy.orm import Session
from database import get_db
from models import ShortenedUrl
app = FastAPI()


@app.post("/urls/", response_model=ShortenedUrlResponse)
def create_shortened_url(url_data: ShortenedUrlCreate, db: Session = Depends(get_db)):
    # Check if the original URL is already in the database
   
    # Create a new shortened URL
    new_url = ShortenedUrl(original_url=str(url_data.original_url), short_link="None")
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)