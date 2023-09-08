A simple program built in Python to simulate how an IoT device communicates over the internet using HiveMQ WebSocket as a Broker.

In this case, sensor_device.py is the Publisher (which means that it sends data to the broker) and the subscribers (receivers) get the data from the broker. When the data is received by the subscriber (computer.py) it will send back an ACK (Acknowledgement) that it has received the data, which then the sensor_device.py will get a success code and continue sending the next batch of data.


Built using Paho MQTT Library.

main.py is what you can start with if you have trouble understanding how the two seperate python files work.

main.py sends generated data to the broker at HiveMQ WebSocket and the topic (category) is temperature/1 and once it sends the data it will subscribe to the topic and receive the data it just sent. This will occur for 3 publishes and stop the program.
