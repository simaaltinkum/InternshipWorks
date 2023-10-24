import paho.mqtt.client as paho
import time
import threading


broker = "iothook.com"
port = 1883
topic = "test2"
print("s")


def publish(client):
    print("publish")
    while True:
        userdata = input("Login a number: ")
        ret = client.publish(topic, userdata)
        print(ret)
        time.sleep(1)


def on_publish(client, userdata, result):
    print("on_publish")


def on_connect(client2, userdata, flags, rc):
    print(f"Connection status: {rc}")
    if rc == 0:
        client2.subscribe("test2")
    else:
        print("Connection failed.")


def on_message(client2, userdata, message):
    print(f"Subject: {message.topic} - Message: {message.payload}")


client = paho.Client()
client2 = paho.Client()
client.username_pw_set("iothookpublic", "iothookpublic")
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)


publish_thread = threading.Thread(target=publish, args= [client])
publish_thread.start()

publish_thread = threading.Thread(target=on_connect, args= [client2])
publish_thread.start()
client.loop_forever()
