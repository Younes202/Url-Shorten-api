# main.py
from fastapi import FastAPI, HTTPException
from schemas import ShortenURLRequest, ShortenURLResponse
from utils import URLShortener, route_url

app = FastAPI()
shortener = URLShortener()


@app.post("/shorten/", response_model=ShortenURLResponse)
async def shorten_url(request: ShortenURLRequest):
    original_url = request.long_url  # Update attribute name to long_url
    shortened_url = route_url(original_url, shortener)
    if not shortened_url:
        raise HTTPException(status_code=400, detail="Invalid URL format")
    return {"shortened_url": shortened_url}