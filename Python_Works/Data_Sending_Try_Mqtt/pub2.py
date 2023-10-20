import sys
import paho.mqtt.client as mqtt

broker = "iothook.com"
port = 1883
topic = "simaltinkum"

while True:
    client = mqtt.Client()
    client.connect(broker, port)
    data = "try"
    client.publish(topic, "%s" %data) # publish
    client.disconnect()