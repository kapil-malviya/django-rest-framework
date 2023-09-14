'''
This is a separate application who wants to connect to our 
api application.

'''


import requests

#URL = 'http://127.0.0.1:8000/all/'
URL = 'http://127.0.0.1:8000/all/6'

values = requests.get(URL)

data = values.json()

print(values)
print(data)