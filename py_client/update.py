import requests
url = "http://localhost:8000/api/products/5/update/"

json = {
    "title":"Book Dan"
}
response = requests.put(url,json=json)

print(response.json())
