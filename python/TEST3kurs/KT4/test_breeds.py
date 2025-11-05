import requests

BASE_URL = "https:/dog.ceo/all"

def test_ger_breeds_success():
    resp = requests.get(f"{BASE_URL}/breeds/list/all")
    assert resp.status_code == 200
    data=resp.json()
    assert data["status"] == "success"

def test_ger_breeds_success():
    resp = requests.get(f"{BASE_URL}/breeds/list/all")
    breeds = resp.json()["message"]
    assert len(breeds) > 0 
