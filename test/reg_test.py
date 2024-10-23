import requests

data = {
        "username": "daft",
        "email": "a@gmail.com",
        "profile": {
            "info": "i am a man",
            "avatar": None
        },
        "password": "canti0-5"
}

response = requests.post("http://127.0.0.1:8000/Profile/", json=data)
print(response.status_code)
print(response.text)