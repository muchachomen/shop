import requests

data = {
    "name": "grains"
}

response = requests.post("http://127.0.0.1:8000/category/", json=data)
print(response.status_code)
print(response.text)