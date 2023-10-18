import requests

# read api key
API_KEY = '3a124c81cfc08b5c3dfa28cc' # demo account #100 Demo Data HTTP Temperature sensor

url = 'https://iothook.com/api/device/?api_key=' + API_KEY

response = requests.get(url)
data = response.json()

file_path = 'doc.txt'

with open(file_path, 'w') as file:
    file.write(str(data))

print(data)
# print(data['datas'][0]['id'])
# print(data['datas'][0]['pub_date'])