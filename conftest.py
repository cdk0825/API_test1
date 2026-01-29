import pytest
from api_client import PostAPI

@pytest.fixture
def post_api():
    return PostAPI("https://jsonplaceholder.typicode.com")

@pytest.fixture
def payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1,
        "id": 1
    }