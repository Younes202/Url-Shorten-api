from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_redirect():
    # Replace "f_CI9ks" with the short link you want to test
    short_link = "f_CI9ks"
    response = client.get(f"/{short_link}")

    # Ensure that the status code is 307 Temporary Redirect
    assert response.status_code == 307

    # Ensure that the Location header in the response redirects to the correct original URL
    expected_redirect_url = "https://www.linkedin.com/events/7167631775039512577/comments/"
    assert response.headers.get("Location") == expected_redirect_url
