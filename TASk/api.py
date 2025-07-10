import requests
payload = {"id": [21,22,24]}
data = requests.get("https://api.sampleapis.com/coffee/hot")
salam = data.json()
print(data.json())