from pydantic import BaseModel
from typing import Dict


class ShortenURLRequest(BaseModel):
    long_url: str


class ShortenURLResponse(BaseModel):
    short_url: str


class CustomURLRequest(BaseModel):
    long_url: str
    custom_short_url: str


class CustomURLResponse(BaseModel):
    message: str


class AnalyticsResponse(BaseModel):
    short_url: str
    clicks: int
    referrers: Dict[str, int]
    user_agents: Dict[str, int]
