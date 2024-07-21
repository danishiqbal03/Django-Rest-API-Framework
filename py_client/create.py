import requests

header = {"Authorization": "Bearer 848d7ae54719a79a74588f19eb3914cef03d9956"}
url = "http://localhost:8000/api/products/"

response = requests.post(url, json={"title": "Danish"}, headers=header)


print(response.json())
