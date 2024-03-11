from fastapi.testclient import TestClient
from .main import app
client = TestClient(app)


def test_create():
    with TestClient(app) as client:
        url = "https://daqsasasaaqqqq.com"
        response = client.post(
            "/urls/",
            headers={"Content-Type": "application/json"},
            json={"original_url": url},
        )
        assert response.status_code == 200
        short_link = response.json()["short_link"]
        redirect_response = client.get(f"/{short_link}")
        assert redirect_response.status_code in {301, 302}  # Allow for both 301 (Moved Permanently) and 302 (Found)
