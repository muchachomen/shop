import requests

data = {

    "comment": "GOOD",
    "rate": 5,
    "product": 2



}


response = requests.post("http://127.0.0.1:8000/review/", json= data)
print(response.status_code)
print(response.text)