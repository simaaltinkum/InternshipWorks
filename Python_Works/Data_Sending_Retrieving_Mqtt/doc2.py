import paho.mqtt.client as paho

broker = "iothook.com"
port = 1883
topic = "test2"
print("s")


def on_connect(client, userdata, flags, rc):
    print("on_connect ", str(rc))
    print(userdata)
    client.subscribe(topic, qos=0)


def on_message(client, userdata, msg):
    print("on_message", msg.topic, str(msg.payload))
    print(msg.payload[0])
    if msg.payload[0] == 97:
        ret = client.publish(msg.topic, msg.payload)

    else:
        print("can not publish")



client = paho.Client()
client.username_pw_set("iothookpublic", "iothookpublic")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)
client.loop_forever()

