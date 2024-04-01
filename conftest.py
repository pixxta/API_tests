import pytest
from api.api_client import APIClient


@pytest.fixture(scope="module")
def api_client():
    return APIClient('https://api.restful-api.dev')


@pytest.fixture(scope="function")
def test_object(api_client):
    obj = {
        "name": "Xiaomi Poco X3",
        "data": {
            "color": "Dark black",
            "capacity": "256 GB"
        }
    }
    created_object = api_client.create_object(obj).json()
    yield created_object
    api_client.delete_object(created_object['id'])
