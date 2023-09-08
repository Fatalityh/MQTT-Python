# Source: Paho MQTT documentation (https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
# Source: Google etc..

import paho.mqtt.client as mqtt  # Import Paho MQTT client library
import time  # Import time library
import json  # Import json library
import random  # Import random library


# Callback when the device successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


# Callback when the device receives a message from the broker
def on_message(client, userdata, message):
    print(f"Acknowledgment Received: {message.payload.decode('utf-8')}")


# Main function for establishing the MQTT connection
def connection():
    # Broker details
    broker_address = "broker.hivemq.com" # This is to the Websocket at: https://www.hivemq.com/demos/websocket-client/
    port = 1883
    message_id = 0  # Initialize message_id

    # Initialize MQTT client
    client = mqtt.Client("SensorDevice")
    client.on_connect = on_connect  # Assign on_connect function
    client.on_message = on_message  # Assign on_message function

    # Try connecting to broker
    try:
        client.connect(broker_address, port)
    except:
        print("Could not connect to MQTT broker")
        return

    # Start the client loop
    client.loop_start()

    # Subscribe to acknowledgment messages
    client.subscribe("temperature/ack")

    # Publish three messages to simulate a sensor
    while message_id < 3:
        message_id += 1

        # Generate random payload data
        temperature = random.randint(20, 50)
        port_channel = random.randint(1, 4)
        rssi = random.randint(-50, -10)
        snr = random.randint(-10, 10)

        # Prepare the payload
        payload = {
            'app_id': 'h20auaji',
            'dev_id': 'TempSensor1',
            'port/channel': port_channel,
            'rssi': rssi,
            'snr': snr,
            'sf': 'TS01921785',
            'C_F': 'C',
            'temperature': temperature,
            'message_id/counter': message_id,
            'time': time.strftime("%H:%M:%S")
        }

        # Convert payload to JSON and publish
        payload_json = json.dumps(payload)
        client.publish("temperature/up", payload_json)
        print(f"Message id: {message_id} sent.")

        # Sleep for 4 seconds before sending the next message
        time.sleep(4)

    # Stop the client loop
    client.loop_stop()


# Main entry point of the script
if __name__ == '__main__':
    connection()
