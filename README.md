# Mqtt-reader

choker run -it --name dockerbroker -v ./config:/mosquitto/config/ eclipse-mosquitto:latest

docker build -t mqttsubc .

docker run -it mqttsubc

mosquitto_pub -h localhost -p 1883 -t "/events" -m '{"sensor_value":20.5}'
