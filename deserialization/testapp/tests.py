from django.test import TestCase

# Create your tests here.

import requests
import json 

URL = 'http://127.0.0.1:8000/createmanager/'

data = {
		'name':'kapil',
		'email':'kapil@malviya.com',
		'age':28,
		'city':'Hyderabad'
}


jsondata = json.dumps(data)
r = requests.post(url=URL, data=jsondata)

data = r.json()
print(data)