import paho.mqtt.client as mqtt
import time


broker = "iothook.com"
port = 1883
topic = "test2"


def on_connect(client, userdata, flags, rc):
    print(f"Bağlantı durumu: {rc}")
    if rc == 0:
        client.subscribe("test2")
    else:
        print("Bağlantı başarısız.")


def on_message(client, userdata, message):
    print(f"Konu: {message.topic} - Mesaj: {message.payload}")


def increase(client, userdata):
    userdata = userdata + 1


def publish(client, userdata):
    print("publish")
    ret = client.publish(topic, userdata)
    print(ret)
    time.sleep(1)


while True:
    client = mqtt.Client("clientId-HNOt0ZhMl3")
    client.username_pw_set("iothookpublic", "iothookpublic")
    client.on_message = on_message
    client.on_connect = on_connect

    print("connecting to broker")
    client.connect(broker, port)

    client.subscribe("test2")
    client.loop_forever()