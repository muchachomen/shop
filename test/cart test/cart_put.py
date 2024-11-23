import requests

data = {
    "products": 2,
    "availability": 20,
    "user": 1
}

response = requests.put("http://127.0.0.1:8000/admins/cart/3/", json=data)
print(response.status_code)
print(response.text)