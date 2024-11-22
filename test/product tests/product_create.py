import requests

data = {

        "name": "Onegin",
        "description": "norm istoria",
        "cost": 12,
        "category": 2,
        "availability": 30


}
file_path = 'AI.png'
with open(file_path, "rb") as f:
    files = {"image": f}

    response = requests.post("http://127.0.0.1:8000/api/products/", data= data, files = files)
print(response.status_code)
print(response.text)