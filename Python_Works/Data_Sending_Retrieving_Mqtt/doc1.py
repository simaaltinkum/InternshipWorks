import paho.mqtt.client as paho
import time

broker = "iothook.com"
port = 1883
topic = "test2"
print("s")

def publish():
    print("publish")
    num = input("Login a number: ")
    ret = client.publish(topic, num)
    print(ret)
    time.sleep(1)


def on_publish(client, userdata, result):
    print("on_publish")


def on_connect(client, userdata, flags, rc):
    print(f"Connection status: {rc}")
    if rc == 0:
        client.subscribe("test2")
    else:
        print("Connection failed.")


def on_message(client, userdata, message):
    print(f"Konu: {message.topic} - Mesaj: {message.payload}")


def control(client, userdata, num):
    if userdata == num + 1 :
        print("True")
        ret = client.publish(topic, num)
        print(ret)
        time.sleep(1)

    else:
        print("False")


while True:
    client = paho.Client()
    client.username_pw_set("iothookpublic", "iothookpublic")
    client.on_publish = on_publish
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    publish()
    # control()
    client.loop_forever()