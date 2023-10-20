import paho.mqtt.client as paho
import time

broker = "iothook.com"
port = 1883
topic = "simaltinkum"
msg_count = 1

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

while True:
    msg = f"messages: {msg_count}"
    client = paho.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()  # Start the MQTT loop
    result = client.publish(topic, msg)
    print(result)
    status = result[0]
    time.sleep(1)

    if status == 0:
        print(f"Send '{msg}' to topic '{topic}'")

    else:
        print(f"Failed to send message to topic {topic}")

    msg_count += 1

    if msg_count > 5:
        break
