import requests

data = {


}



response = requests.post("http://127.0.0.1:8000/payment/", json= data)
print(response.status_code)
print(response.text)