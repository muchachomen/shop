import requests

response = requests.delete("http://127.0.0.1:8000/admins/products/2/")
print(response.status_code)
print(response.text)