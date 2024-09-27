# Mqtt-reader

docker-compose up

docker build -t mqttsubc .

docker run -it mqttsubc

mosquitto_pub -h localhost -p 1883 -t "/events" -m '{"sensor_value":20.5}'
