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

def on_connect(client, userdata, flags, rc):
    print(f"Connection status: {rc}")
    if rc == 0:
        client.subscribe("test2")
    else:
        print("Connection failed.")

def on_message(client, userdata, message):
    print(f"Subject: {message.topic} - Message: {message.payload}")

def control(client, userdata, num):
    if userdata == num + 1:
        print("True")
        ret = client.publish(topic, num)
        print(ret)
        time.sleep(1)
    else:
        print("False")

"""def mqtt_client_thread(client):
    
    client.username_pw_set("iothookpublic", "iothookpublic")
    client.on_publish = on_publish
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_forever()"""

client = paho.Client()
client.username_pw_set("iothookpublic", "iothookpublic")
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)


"""mqtt_thread = threading.Thread(target=mqtt_client_thread, args=[client])
mqtt_thread.start()"""


publish_thread = threading.Thread(target=publish, args= [client])
publish_thread.start()
client.loop_forever()

"""mqtt_thread.join()
publish_thread.join()"""
