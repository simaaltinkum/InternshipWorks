import threading
import paho.mqtt.client as paho

broker = "iothook.com"
port = 1883
topic = "test2"
print("s")

def sub_thread_def():
    def on_connect(client, userdata, flags, rc):
        print("on_connect ", str(rc))
        client.subscribe(topic)


    def on_message(client, userdata, msg):
        print("on_message", msg.topic, str(msg.payload))

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

sub_thread = threading.Thread(target=sub_thread_def)
sub_thread.start()
print("smmmmmmm")
