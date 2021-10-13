#import hashlib
#print(hashlib.md5(b"test").hexdigest())


import requests
from requests.models import Response

url = 'http://localhost:5000/api/login'
obj = {'ip':'192.168.3.10','id':'Door'}

resp = requests.post(url, obj)

print(resp.text)