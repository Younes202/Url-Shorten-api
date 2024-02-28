from fastapi import HTTPException


class URLNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Short URL not found")


class CustomURLAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Custom short URL already exists")


class InvalidURLException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Invalid URL format")
