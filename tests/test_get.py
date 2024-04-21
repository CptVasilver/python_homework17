import json
import requests
from jsonschema import validate
from resource import path


def test_get_api_get_nonexistent_user():
    url = "https://reqres.in/api/users/13"

    response = requests.request("GET", url)

    assert response.status_code == 404
    assert response.json() == {}


def test_get_api_get_real_user():
    url = "https://reqres.in/api/users/12"

    response = requests.request("GET", url)

    assert response.status_code == 200

    with open(path('get_users.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))
