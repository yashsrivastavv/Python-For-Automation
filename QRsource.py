import requests
import json
# from requests.models import Response
url = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '9771234567003'}

response = requests.get(url, params = parameters)
print(response.url)
content = response.content

info = json.loads(content)
print(type(info))
print(info)
item = info['items']
itemInfo = item [0]
title =itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)
