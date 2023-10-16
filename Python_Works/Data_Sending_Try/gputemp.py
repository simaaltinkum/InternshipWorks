import wmi
import json
import requests

def get_gpu_temperature():
    c = wmi.WMI(namespace="root\\OpenHardwareMonitor")
    temperature_info = c.Sensor()

    for sensor in temperature_info:
        if sensor.SensorType == "Temperature" and "GPU" in sensor.Name:
            return sensor.Value

gpu_temperature = get_gpu_temperature()
if gpu_temperature is not None:
    print(f"GPU Sıcaklığı: {gpu_temperature}°C")

    headers = {'Content-type': 'application/json'}
    API_KEY = '3a124c81cfc08b5c3dfa28cc'
    url = 'http://iothook.com/api/update/' + API_KEY

    data = {
        'api_key': API_KEY,
        'field_1': gpu_temperature,
    }

    data_json = json.dumps(data)

    response = requests.post(url, data=data_json, headers=headers)
    print(response.json())
else:
    print("GPU sıcaklık verisi bulunamadı.")
