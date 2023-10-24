import paho.mqtt.client as mqtt
import time
import threading

broker = "iothook.com"
port = 1883
topic = "test2"
userdata = 0

def on_connect(client, userdata, flags, rc):
    print(f"Connection status: {rc}")
    if rc == 0:
        client.subscribe("test2")
    else:
        print("Connection failed.")

def on_message(client, userdata, message):
    print(f"Subject: {message.topic} - Message: {message.payload}")

def publish(client):  
    global userdata
    print("publish")
    userdata += 1
    ret = client.publish(topic, userdata)
    print(ret)
    time.sleep(1)

def on_publish(client, userdata, result):
    print("on_publish")

def mqtt_thread():
    client = mqtt.Client("clientId-HNOt0ZhMl3")
    client.username_pw_set("iothookpublic", "iothookpublic")
    client.on_publish = on_publish
    client.on_message = on_message
    client.on_connect = on_connect

    print("connecting to broker")
    client.connect(broker, port)
    client.subscribe("test2")
    client.loop_start()

    while True:
        publish(client)
        time.sleep(1)

if __name__ == "__main__":
    mqtt_thread = threading.Thread(target=mqtt_thread)
    mqtt_thread.start()
    mqtt_thread.join()
