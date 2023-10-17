import json
import pprint
import time
import psutil
import requests

headers = {'Content-type': 'application/json'}

# demo account API_KEY
# https://iothook.com/en/device/data/100/
# 100 - Demo Data HTTP
API_KEY = 'bffd5360f95928bead85ded5'  # write api key
url = 'http://iothook.com/api/update/'
a,b,c,d,e= psutil.cpu_times()

for i in range(5):
    data = {  # write api key
        'api_key': API_KEY,  # demo hesap #100 - Demo Data HTTP
        'field_1': b,
        'field_2': a,
        'field_3': c,
        'field_4': d,
        'field_5': e
    }

    data_json = json.dumps(data)

    response = requests.post(url, data=data_json, headers=headers)
    pprint.pprint(response.json())
    time.sleep(15)