import requests

data = {
    "name": "tomato",
    "description": "very taste",
    "cost": 2222,
    "category": 1,
    "image": "AI.png",
    "availability": 22

}

response = requests.post("http://127.0.0.1:8000/product/", json= data)
print(response.status_code)
print(response.text)