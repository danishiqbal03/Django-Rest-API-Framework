import requests
url = "http://localhost:8000/api/products/2/delete/"

response = requests.delete(url)
