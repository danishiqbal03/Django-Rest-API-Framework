from getpass import getpass

import requests

user = input("Enter Username\n")
passw = getpass(prompt="Enter your Password\n")

endpoint = "http://localhost:8000/api/auth/"
auth_response = requests.post(endpoint, json={"username": user, "password": passw})

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    header = {"Authorization": f"Bearer {token}"}
    print(header)
    url = "http://localhost:8000/api/products/"
    response = requests.get(url, headers=header)
    print(response.json())
