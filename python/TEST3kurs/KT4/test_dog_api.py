import requests
import pytest

BASE_URL = "https://dog.ceo/api"

# 1. Тест получения случайного изображения собаки
def test_random_dog_image():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert data["message"].startswith("https://")

# 2. Тест списка всех пород
def test_all_breeds_list():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], dict)
    assert "bulldog" in data["message"]

# 3. Тест случайного изображения для конкретной породы
def test_random_image_by_breed():
    breed = "bulldog"
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert "bulldog" in data["message"]

# 4. Тест случайного изображения для подтипа породы
def test_random_image_by_sub_breed():
    breed = "bulldog"
    sub_breed = "french"
    response = requests.get(f"{BASE_URL}/breed/{breed}/{sub_breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert f"{breed}-{sub_breed}" in data["message"] or breed in data["message"]

# 5. Тест на обработку несуществующей породы
def test_invalid_breed():
    response = requests.get(f"{BASE_URL}/breed/invalidbreed/images/random")
    assert response.status_code in [404, 200]
    data = response.json()
    assert "status" in data
