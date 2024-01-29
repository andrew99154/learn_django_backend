import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

auth_response = requests.post(auth_endpoint, json={"username": "andrew", "password": "junyi99154"})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    print(token)
    headers = {"Authorization": "Bearer " + token}
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
