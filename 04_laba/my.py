import requests

r = requests.get('https://httpbin.org/')
print(r.encoding)

