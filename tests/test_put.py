import json
import requests
from jsonschema import validate
from resource import path


def test_put_api_change_user_data():
    url = "https://reqres.in/api/users"

    payload = {'job': 'Guard',
               'name': 'Samuel',
               'surname': 'Vimes'}

    id = requests.request("POST", url, data=payload).json()['id']

    new_payload = {'job': 'Guard',
                   'name': 'Samuel',
                   'surname': 'Vimes-Ownec'}
    response = requests.request("PUT", f'{url} + "/" + {id}', data=new_payload)

    assert response.status_code == 200

    with open(path('put_users.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))
