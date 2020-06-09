import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


broker_address = "163.180.117.202:1883"
client = mqtt.Client("Client")
client.on_message = on_message
client.connect(broker_address)
client.loop_start()
client.subscribe("introduction/greeting")
client.publish("introduction/greeting", "hello")
time.sleep(4)
print("finish")
client.loop_stop()
