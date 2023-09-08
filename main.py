# Source: Paho MQTT documentation (https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
# Source: Google etc..

import paho.mqtt.client as mqtt
import time
import json
import random

# When connected, will give result code.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Prints back the message that was published to Broker.
def on_message(client, userdata, message):
    print("Message Received ", str(message.payload.decode("utf-8")))

def connection():
    broker_address = "broker.hivemq.com" # This is to the Websocket at: https://www.hivemq.com/demos/websocket-client/
    port = 1883
    message_id = 0 # This will be used for the ID of the message. For example in 1.2 we use this to use it as a validation ID for ACK.

    # Initialize the MQTT client
    client = mqtt.Client("P1")
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to broker
    client.connect(broker_address, port)
    client.loop_start() # Basically a MQTT Loop

    client.subscribe("temperature/1")

    while message_id < 3:
        message_id += 1  # Increment message ID

        # Generate random values
        temperature = random.randint(20, 50)
        port_channel = random.randint(1, 4)
        rssi = random.randint(-50, -10)
        snr = random.randint(-10, 10)

        payload = {
            'app_id': 'h20auaji',
            'dev_id': 'TempSensor1',
            "port/channel": port_channel,
            "rssi": rssi,
            "snr": snr,
            "sf": "TS01921785",
            "C_F": "C",
            "temperature": temperature,
            "message id/counter": message_id,
            'time': time.strftime("%H: %M: %S")
        }

        payload_json = json.dumps(payload)
        client.publish("temperature/1", payload_json)

        print(f"Message id: {message_id} sent.")

        if message_id >= 3:
            break  # Exit loop after 3 publishes

        time.sleep(4)  # Sleep for 4 seconds before sending the next message

    client.loop_stop()

if __name__ == '__main__':
    connection()
