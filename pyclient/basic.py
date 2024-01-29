import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello World", "content":"haha", "price":1287})
print(get_response.json())
