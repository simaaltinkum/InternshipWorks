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


def control(client, userdata, num):
    if userdata == num+1 :
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
    client.connect(broker, port)
    publish()
    # control()
    client.loop_forever()