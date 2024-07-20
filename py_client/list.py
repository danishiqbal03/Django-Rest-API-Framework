import requests
url = "http://localhost:8000/api/products/"

response = requests.get(url)


print(response.json())
