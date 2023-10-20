import paho.mqtt.client as paho
import time

broker = "iothook.com"
port = 1883
topic = "simaltinkum"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

while True:
    client = paho.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()  # Start the MQTT loop
    t = int(time.time())
    ret = client.publish(topic, "%s" % t, qos=0, retain=False)  # publish
    print(ret)
    time.sleep(1)
