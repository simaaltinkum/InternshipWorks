import paho.mqtt.client as paho
import time
import threading


broker = "iothook.com"
port = 1883
topic = "test2"
print("s")
userdata = None

def on_publish(client, user_data, result):
    print("on_publish")

def publish_thread_def():
    print("publish_thread_def çalıştı")
    global userdata

    client = paho.Client()
    client.username_pw_set("iothookpublic", "iothookpublic")
    client.on_publish = on_publish
    client.connect(broker, port)

    while True:
        userdata = input("Login a number: ")
        client.publish(topic, userdata)
        time.sleep(1)
    # client.loop_forever()


def subscriber_thread_def():
    print("subscriber thr def çalıştı")

    def on_connect(client, userdata, flags, rc):
        print(f"Connection status: {rc}")
        if rc == 0:
            client.subscribe("test2")
        else:
            print("Connection failed.")

    def on_message(client, userdata, message):
        print(f"Subject: {message.topic} - Message: {message.payload}")

    client = paho.Client()
    client.username_pw_set("iothookpublic", "iothookpublic")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    # client.loop_forever()
    client.subscribe("test2")


publish_thread = threading.Thread(target=publish_thread_def)
publish_thread.start()

subscriber_thread = threading.Thread(target=subscriber_thread_def)
subscriber_thread.start()
print("11111111111111")

