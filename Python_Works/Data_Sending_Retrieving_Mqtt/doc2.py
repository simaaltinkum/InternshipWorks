import paho.mqtt.client as mqtt
import time

broker = "iothook.com"
port = 1883


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))


client = mqtt.Client("clientId-sampomjx7S")
client.username_pw_set("iothookpublic", "iothookpublic")
client.on_message = on_message

print("connecting to broker")
client.connect(broker, port)

client.subscribe("test2")

client.loop_forever()