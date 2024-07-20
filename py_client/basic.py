import requests
url = "http://localhost:8000/api/"

params = {"query": "Iqbal"}
# response = requests.get(url, params=params)
response = requests.post(url, json={"title":None})


print(response.json())  # Converts JSON-based API response to a Python dictionary
