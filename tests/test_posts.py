def test_get_all(post_api):
    response = post_api.get_all()
    
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert isinstance(response.json(), list)

def test_create_post(post_api, payload):
    # payload = {"title": "foo", "body": "bar", "userId": 1}
    
    response = post_api.create(payload)
    
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
    assert "id" in response.json()
    
def test_update_post(post_api):
    payload = {"title": "update title"}
    
    response = post_api.update(1, payload)
    
    assert response.status_code == 200
    assert response.json()["title"] == "update title"
    
    
def test_delete(post_api):
    responce = post_api.delete(1)
    
    assert responce.status_code == 200