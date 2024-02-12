import random
import json
import pprint
import time
import psutil
import requests

def lamba_yak():
    while True:
        lamba = random.randint(0,2)

        kirmizi = False
        yesil = False
        sari = False

        if lamba == 0:
            kirmizi = True
            print('kırmızı yanıyor')

        elif lamba == 1:
            yesil == True
            print('yeşil yanıyor')

        else:
            sari = True
            print('sarı yanıyor')

        headers = {'Content-type': 'application/json'}

        # demo account API_KEY
        # https://iothook.com/en/device/data/100/
        # 100 - Demo Data HTTP
        API_KEY = '1c1094835fe305ad04096223'  # write api key
        url = 'http://iothook.com/api/update/'
        kirmizi, yesil, sari = psutil.cpu_times()

        for i in range(3):
            data = {  # write api key
                'api_key': API_KEY,  # demo hesap #100 - Demo Data HTTP
                'kırmızı': kirmizi,
                'yeşil': yesil,
                'sarı': sari,
            }

            data_json = json.dumps(data)

            response = requests.post(url, data=data_json, headers=headers)
            pprint.pprint(response.json())
            time.sleep(1)
lamba_yak()
