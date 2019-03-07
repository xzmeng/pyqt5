from urllib.parse import urlencode

import requests
import json


url = 'http://web.juhe.cn:8080/environment/air/cityair'

params = {
    'city': '郑州',
    'key': 'bae9fd7d6958840b5f31f0ab49bb537c',
}

r = requests.get(url, params)
d = json.loads(r.content)
print(d)
print(d.get('result')[0].get('citynow').get('AQI'))
