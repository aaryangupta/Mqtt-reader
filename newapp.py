import asyncio
from gmqtt import Client as MQTTClient

BROKER_HOST = 'host.docker.internal'  # Update this with your broker's address if necessary
BROKER_PORT = 1883
TOPIC = '/events'

# Define an asynchronous MQTT client
class MyMQTTClient:

    def __init__(self, client_id):
        self.client = MQTTClient(client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe

    async def connect(self):
        # Connect to the MQTT broker
        await self.client.connect(BROKER_HOST, BROKER_PORT)

    async def subscribe(self, topic):
        # Subscribe to the topic
        self.client.subscribe(topic)

    def on_connect(self, client, flags, rc, properties):
        print(f'Connected with result code {rc}')

    def on_message(self, client, topic, payload, qos, properties):
        print(f'Received message on {topic}: {payload.decode()}')

    def on_disconnect(self, client, packet, exc=None):
        print(f'Disconnected from MQTT Broker')

    def on_subscribe(self, client, mid, qos, properties):
        print(f'Subscribed to {TOPIC}')

    async def start(self):
        await self.connect()
        await self.subscribe(TOPIC)
        # Keep the connection alive
        await asyncio.Event().wait()

# Async entry point
async def main():
    mqtt_client = MyMQTTClient(client_id='my-client-id')
    await mqtt_client.start()

if __name__ == '__main__':
    asyncio.run(main())
