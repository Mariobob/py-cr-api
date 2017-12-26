import json
import requests

url = f"https://api.cr-api.com/profile/{tag]"
headers = {"auth": auth_key}
response = requests.get(url, headers=headers)
resp_json = response.json()

def profile():
    print(resp_json['name'])
