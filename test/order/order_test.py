import requests

data ={
    "product": 4,
    "method": 1
}


response = requests.post("http://127.0.0.1:8000/api/orders/", json= data)
print(response.status_code)
print(response.text)