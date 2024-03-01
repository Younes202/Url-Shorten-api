from pydantic import BaseModel, HttpUrl


class ShortenedUrlCreate(BaseModel):
    original_url: HttpUrl


class ShortenedUrlResponse(BaseModel):
    id: int
    original_url: HttpUrl
    short_link: str


class ShortLinkResponse(BaseModel):
    short_link: HttpUrl


class User(BaseModel):
    id: int
    name: str
    role: str
