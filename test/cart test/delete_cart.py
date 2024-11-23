import requests

response = requests.delete("http://127.0.0.1:8000/admins/cart/3/")
print(response.status_code)
print(response.text)