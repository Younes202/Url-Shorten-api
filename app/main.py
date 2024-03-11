from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from datetime import datetime, timezone
from .schemas import ShortenedUrlCreate, ShortLinkResponse
from sqlalchemy.orm import Session
from .database import get_db
from app.models import ShortenedUrl
from .utils import create_short_link
from sqlalchemy.exc import IntegrityError
from .exceptions import UrlAlreadyExistsException, InternalBackendError
app = FastAPI()


@app.post("/urls/", response_model=ShortLinkResponse)
def create_shortened_url(url_data: ShortenedUrlCreate, db: Session = Depends(get_db)):
    try:
        timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()
        short_link = create_short_link(url_data.original_url, timestamp)
        new_url = ShortenedUrl(original_url=str(url_data.original_url), short_link=short_link)
        db.add(new_url)
        db.commit()
        db.refresh(new_url)
        return ShortLinkResponse(short_link=short_link)
    except IntegrityError as e:
        if "duplicate key value" in str(e.orig):
            raise UrlAlreadyExistsException()
        else:
            raise InternalBackendError()


@app.get("/{short_link}")
def redirect(short_ln: str, db: Session = Depends(get_db)):
    obj = db.query(ShortenedUrl).filter_by(short_link=short_ln).first()
    if obj is None:
        raise HTTPException(
            status_code=404, detail="The link does not exist, could not redirect."
        )
    return ShortLinkResponse(short_link=obj.original_url)
