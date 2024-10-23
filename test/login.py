import requests

data ={
    "username": "f",
    "password": "f"
}

response = requests.post("http://127.0.0.1:8000/api/token/", json=data)
print(response.status_code)
print(response.text)