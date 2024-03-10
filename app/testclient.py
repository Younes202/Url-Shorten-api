from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_create_shortened_url():
    # Test creating a shortened URL
    url = "https://example.com"
    response = client.post("/urls/", json={"original_url": url})
    # Ensure that the response status code is 201 for successful creation
    assert response.status_code == 201
    short_link = response.json()["short_link"]

    # Test redirection using the created short_link
    redirect_response = client.get(f"/{short_link}")
    # Ensure that the redirection response status code is 301 (redirect)
    assert redirect_response.status_code == 301
