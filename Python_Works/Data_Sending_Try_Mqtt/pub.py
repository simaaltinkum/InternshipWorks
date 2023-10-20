import paho.mqtt.client as paho
import time

broker = "iothook.com"
port = 1883
topic = "simaltinkum"

if __name__ == "__main__":
    client = paho.Client()
    client.connect(broker, port)
    t = int(time.time())
    ret = client.publish(topic, "%s" % t)  # publish
    print(ret)
    time.sleep(1)