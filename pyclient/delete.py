import requests
product_id = input("the id you want to delete:")
try:
    product_id = int(product_id)
except:
    print(f"{product_id} is not valid id")
    product_id = None
    
if product_id is not None:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)
    if get_response.status_code == 204:
        print("delete successfully")
    else: print(get_response.json())
