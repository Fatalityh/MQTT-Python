# Source: Paho MQTT documentation (https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
# Source: Google etc..

import paho.mqtt.client as mqtt  # Import Paho MQTT client library
import json  # Import json library


# Callback when the computer successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected to broker with result code {rc}")


# Callback when the computer receives a message from the broker
def on_message(client, userdata, message):
    try:
        # Decode and load JSON payload
        received_payload = json.loads(message.payload.decode("utf-8"))

        # Print received message
        print(
            f"Received Message with ID {received_payload['message_id/counter']}, Temperature: {received_payload['temperature']}, Time: {received_payload['time']}")

        # Acknowledge the message by sending an ACK
        ack_payload = {'ack_for_message_id': received_payload['message_id/counter']}
        ack_payload_json = json.dumps(ack_payload)
        client.publish("temperature/ack", ack_payload_json)
        print(f"Sent ACK for message id {received_payload['message_id/counter']}")

    except Exception as e:
        print(f"Error: {e}")


# Initialize MQTT client
client = mqtt.Client("Computer")
client.on_connect = on_connect  # Assign on_connect function
client.on_message = on_message  # Assign on_message function

# Try connecting to broker
try:
    client.connect("broker.hivemq.com", 1883) # This is to the Websocket at: https://www.hivemq.com/demos/websocket-client/
except:
    print("Could not connect to MQTT broker")
    exit(1)

# Start the client loop
client.loop_start()

# Subscribe to temperature messages
client.subscribe("temperature/up")

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
