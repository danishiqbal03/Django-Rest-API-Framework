import requests
url = "http://localhost:8000/api/products/4/"

response = requests.get(url)


print(response.json())
