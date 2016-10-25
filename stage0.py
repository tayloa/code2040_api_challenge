import requests
import json

data = {"token" : "24.3", "github" : "token"}
response = requests.post("http://challenge.code2040.org/api/register", json=data)