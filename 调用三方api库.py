import requests

response = requests.get('http://172.22.153.22:9999/getRecord', params={'domain': 'www.xinnet.com', 'type': 'cname'})
print(response.json())
