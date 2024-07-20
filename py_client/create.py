import requests
url = "http://localhost:8000/api/products/"

response = requests.post(url,json={"title":"Book Dawn"})


print(response.json())
