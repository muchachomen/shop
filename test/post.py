import requests

data = {

        "name": "gag",
        "description": "ff",
        "cost": 1,
        "category": 1,
        "availability": 22


}
file_path = 'AI.png'
with open(file_path, "rb") as f:
    files = {"image": f}

    response = requests.post("http://127.0.0.1:8000/product/", data= data, files = files)
print(response.status_code)
print(response.text)