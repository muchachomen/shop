import requests

data = {

    "products": 2,
    "availability": 1,
    "user": 1
}



response = requests.post("http://127.0.0.1:8000/cart/", json= data)
print(response.status_code)
print(response.text)