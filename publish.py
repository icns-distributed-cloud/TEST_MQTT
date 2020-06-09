import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

BROKER_IP = "163.180.117.202"
BROKER_PORT = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("mqtt/pong")


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


if __name__ == "__main__":
    client = mqtt.Client("Publisher")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_IP, BROKER_PORT, 60)

    publish.single("mqtt/ping", "ping", hostname=BROKER_IP, port=BROKER_PORT)

    client.loop_forever()
