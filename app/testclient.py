from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_create_shortened_url():
    # Test creating a shortened URL
    url = "https://example.com"
    response = client.post("/urls/", json={"original_url": url})
    # Ensure that the response status code is 404 for duplicate URL
    assert response.status_code == 404


def test_redirect():
    with TestClient(app) as client:
        short_link = "wHkltvM"
        # Test redirection using the created short_link
        redirect_response = client.get(f"/{short_link}")
        assert redirect_response.status_code == 404
