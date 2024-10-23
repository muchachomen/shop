import requests

data = {
    "product": 4

}

response = requests.post("http://127.0.0.1:8000/cart/", json= data)
print(response.status_code)
print(response.text)