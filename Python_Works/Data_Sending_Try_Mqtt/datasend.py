import paho.mqtt.client as mqtt

# Define MQTT broker and topic
broker = "iothook.com"
port = 1883
topic = "testtopic"

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# Create a MQTT client
client = mqtt.Client()
client.username_pw_set("iothookpublic", "iothookpublic")  # Set your MQTT username and password

# Assign the callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Loop to listen for messages
client.loop_forever()
