import random
import json
import pprint
import time
import psutil
import requests


while True:
    lamba = random.randint(0, 2)

    kirmizi = False
    yesil = False
    sari = False

    if lamba == 0:
        kirmizi = True
        print(int(kirmizi))
        print('kırmızı yanıyor')

    elif lamba == 1:
        yesil = True
        print(int(yesil))
        print('yeşil yanıyor')

    else:
        sari = True
        print(int(sari))
        print('sarı yanıyor')

    headers = {'Content-type': 'application/json'}

    # demo account API_KEY
    # https://iothook.com/en/device/data/100/
    # 100 - Demo Data HTTP
    API_KEY = '456aeebe9c317810fe7b2245'  # write api key
    url = 'https://iothook.com/api/update/?api_key=456aeebe9c317810fe7b2245&field_1=10&field_2=20&field_3=30'

    data = {
        'api_key': API_KEY,
        'field_1': int(kirmizi),
        'field_2': int(yesil),
        'field_3': int(sari),
    }

    print(data)
    data_json = json.dumps(data)

    response = requests.post(url, data=data_json, headers=headers)
    pprint.pprint(response.json())
    # time.sleep(1)