import requests

# read api key
API_KEY = '33cc8bb9a354204dc23900cc' # demo account #100 Demo Data HTTP Temperature sensor

url = 'https://iothook.com/api/device/?api_key=' + API_KEY

response = requests.get(url)
data = response.json()
print(data)
# print(data['datas'][0]['id'])
# print(data['datas'][0]['pub_date'])