import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_list():
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert isinstance(response.json(), list)
    
def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
    assert "id" in response.json()
    
def test_update_post():
    payload = {
        "id": 1,
        "title": "updated",
        "body": "body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    
    assert response.status_code == 200
    assert response.json()["title"] == "updated"
    
def test_partial_update_post():
    payload = {"title": "patched title"}
    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    
    assert response.status_code == 200
    assert response.json()["title"] == "patched title"
    
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200