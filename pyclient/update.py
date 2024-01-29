import requests

endpoint = "http://localhost:8000/api/products/32/update/"

data = {
    "title": "updated",
    "price": 99987
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
