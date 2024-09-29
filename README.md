# Mqtt-reader

TASK
● Make a python program that connects to a Mosquitto MQTT broker, listens for messages
on the topic /events
● Start the Mosquitto MQTT broker from a docker container
● Dockerize your python application and start it.
● Manually publish a message to the topic.



docker run -it --name dockerbroker -v ./config:/mosquitto/config/ eclipse-mosquitto:latest

docker build -t mqttsubc .

docker run -it mqttsubc

mosquitto_pub -h localhost -p 1883 -t "/events" -m '{"sensor_value":20.5}'
