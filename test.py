import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + 'video/3', {'likes': 111, 'author': 'Benjamin'})
print(response.json())