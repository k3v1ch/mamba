import requests

BASE_URL = "https:/dog.ceo/all"

def test_invalid_breed_returns_errors():
    resp =requests.get (f"{BASE_URL}/breed/unknownbreed/image")
    data=resp.json()
    assert data["status"] == "error"