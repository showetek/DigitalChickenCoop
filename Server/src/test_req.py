import requests
from requests.models import Response

url = 'http://localhost:5000/api/login'
obj = {'ip':'1'}

resp = requests.post(url, obj)

print(resp.text)