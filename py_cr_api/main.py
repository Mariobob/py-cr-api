import json
import requests


def get_tag(tag):
    tag = f"https://api.cr-api.com/profile/{tag}"
    
def get_auth(auth_key):
    auth_key = {"auth": auth_key}
    
def profile(tag_var, auth_var):
    url = tag_var
    headers = auth_var
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data['name'])
    
   
