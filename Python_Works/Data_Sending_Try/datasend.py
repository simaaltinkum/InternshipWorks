import json
import random
import time
import requests
import pprint

headers = {'Content-type': 'application/json'}

API_KEY = '3a124c81cfc08b5c3dfa28cc'
url = 'http://iothook.com/api/update/' + API_KEY

for i in range(5):
    data = {
        'api_key': API_KEY,
        'field_1': random.randint(1, 10),
        'field_2': round(random.uniform(0.0, 10.0), 2),
    }

    data_json = json.dumps(data)

    response = requests.post(url, data=data_json, headers=headers)
    pprint.pprint(response.json())
    time.sleep(15)
