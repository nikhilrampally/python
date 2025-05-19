import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://sainikhil2494.atlassian.net/rest/api/3/project"

API_TOKEN= os.getenv("API_TOKEN")

auth = HTTPBasicAuth("sainikhil2494@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)