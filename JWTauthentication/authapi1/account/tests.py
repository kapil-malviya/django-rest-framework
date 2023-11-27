import requests
import json

URL = 'http://127.0.0.1:8000/api/user/login/'

data = {
    'email': 'harshyadav5736@gmail.com',
    'password': 'harshh'
}

headers = {'Content-Type': 'application/json'}  # set Content-Type header to specify JSON data

jsondata = json.dumps(data)
r = requests.post(url=URL, data=jsondata, headers=headers)

data = r.json()
print(data)
