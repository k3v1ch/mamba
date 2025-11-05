import requests
import re

BASE_URL = "https:/dog.ceo/all"
URL_REGEX = re.compile(r"^https?://.*\.(jpg|jpeg|png)$")

def test_random_image_url():
    resp = requests.get(f"{BASE_URL}/breeds/image/random")
    url = resp.json()["message"]
    assert URL_REGEX.match(url)