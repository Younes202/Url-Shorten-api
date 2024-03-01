from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from datetime import datetime, timezone
from .schemas import ShortenedUrlCreate, ShortLinkResponse
from sqlalchemy.orm import Session
from .database import get_db
from .models import ShortenedUrl
from .utils import create_short_link
app = FastAPI()


@app.post("/urls/", response_model=ShortLinkResponse)
def create_shortened_url(url_data: ShortenedUrlCreate, db: Session = Depends(get_db)):
    # Check if the original URL is already in the database
    timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    short_link = create_short_link(url_data, timestamp)
    # Create a new shortened URL
    new_url = ShortenedUrl(original_url=str(url_data.original_url), short_link=short_link)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return ShortLinkResponse(short_link=short_link)
    # return ShortenedUrlResponse(id=new_url.id, original_url=new_url.original_url, short_link=new_url.short_link)


@app.get("/{short_link}")
def redirect(short_link: str, db: Session = Depends(get_db)):
    obj = db.query(ShortenedUrl).filter_by(short_link=short_link).first()
    if obj is None:
        raise HTTPException(
            status_code=404, detail="The link does not exist, could not redirect."
        )
    return RedirectResponse(url=obj.original_url)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
