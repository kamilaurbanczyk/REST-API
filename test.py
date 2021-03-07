import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + 'video/10', {'name': 'Widmo', 'likes': 100, 'author': 'Benjamin', 'views': 1320})
print(response.json())
input()
resp2 = requests.get(BASE + 'video/60')
print(resp2.json())