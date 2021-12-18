#import hashlib
#print(hashlib.md5(b"test").hexdigest())


import requests
from requests.models import Response

url = 'http://localhost:5000/api/login'
obj = {"ip":"192.168.3.10","id":"Door"}

resp = requests.post(url, f'{obj}')

print(resp.text)

import json
print(str({"ip":"192.168.3.10","id":"Door"}))
x = json.loads('{"ip":"192.168.3.10","id":"Door"}')
print(x)
print(x['ip'])
#json.loads()

print(str(obj))
print(json.dumps(str(obj)))