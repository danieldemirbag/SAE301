import paho.mqtt.client as mqtt
from django.shortcuts import render

global test


test = 0
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Courgette/banane/lièvre")
    client.subscribe("Courgette/banane/lièvre2")
    #client.subscribe("ESP2")
    #client.subscribe("ESPT")

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    print(str(msg.payload))
    test = msg.payload

'''''
def print_on_m(request):
    global test
    message = str(test)
    return render(request, 'monweb/mqtt.html',{'context':message})
'''''

def on_publish(client, userdata, result):
    print("data published")
    pass


client = mqtt.Client("ESP2")
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect("test.mosquitto.org", port=1883, keepalive=60)