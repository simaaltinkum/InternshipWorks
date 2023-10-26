import paho.mqtt.client as paho

broker = "iothook.com"
port = 1883
topic = "test2"
print("s")

def on_connect():
    print("on_connect")
    client.subscribe(topic, qos=0)
    print("çıktı")

def on_message(msg):
    print("on_message", msg.topic, str(msg.payload))

    if msg.payload[0] == 97:
        client.publish(msg.topic, msg.payload)

    else:
        print("can not publish")
        print("çıktı msg")



client = paho.Client()
client.username_pw_set("iothookpublic", "iothookpublic")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)
print("burası bitti")
client.loop_start()
# client.loop_forever()

# sub_thread = threading.Thread(target=sub_thread_def)
# sub_thread.start()

# pub_thread = threading.Thread(target=pub_thread_def)
# pub_thread.start()
