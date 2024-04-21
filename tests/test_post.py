import json
import requests
from jsonschema import validate
from resource import path


def test_post_api_create_and_validate_user():
    url = "https://reqres.in/api/users"

    payload = {'job': 'Guard',
               'name': 'Samuel',
               'surname': 'Vimes'}

    response = requests.request("POST", url, data=payload)

    assert response.status_code == 201

    with open(path('post_users.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_post_api_authorization_fail():
    url = "https://reqres.in/api/register"
    response = requests.request("POST", url)

    assert response.status_code == 400

    with open(path('post_registration_error.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))
