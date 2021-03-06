import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

BROKER_IP = "192.168.77.1"
BROKER_PORT = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("mqtt/ping")


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print(type(message.topic))
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

    if message.topic == "mqtt/ping":
        publish.single("mqtt/pong", "pong", hostname=BROKER_IP, port=BROKER_PORT)
        print("here")


if __name__ == "__main__":
    client = mqtt.Client("client1")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_IP, BROKER_PORT, 60)

    client.loop_forever()
