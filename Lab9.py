import json
import requests

r=requests.get('localhost:3000')

data = r.json()

print (data['widget1'][0]['color'])
print (data['widget2'][0]['color'])
print (data['widget3'][0]['color'])
print (data['widgetX'][0]['color'])