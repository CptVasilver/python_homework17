import json
import requests
from jsonschema import validate
from resource import path


def test_delete_api_remove_user():
    url = "https://reqres.in/api/users/1"

    response = requests.request("DELETE", url)

    assert response.status_code == 204
