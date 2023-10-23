import paho.mqtt.client as paho
import time

broker = "iothook.com"
port = 1883
topic = "test2"


def publish():
    print("publish")
    num = input("Login a number: ")
    ret = client.publish(topic, num)
    print(ret)
    time.sleep(1)


def control(client, userdata, num):
    if userdata == num+1 :
        print("True")
        ret = client.publish(topic, num)
        print(ret)
        time.sleep(1)

    else:
        print("False")
    

client = paho.Client()
client.username_pw_set("iothookpublic", "iothookpublic")
client.publish = publish
client.connect(broker, port)
client.loop_forever()