# author: Aaront Taylor
# email: halfnote1004@gmail.com
# Summary: This code posts JSON data to a given api

import requests
import json


data = {"token" : "24.3", "github" : "token"}
response = requests.post("http://challenge.code2040.org/api/register", json=data)