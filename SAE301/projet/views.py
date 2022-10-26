from django.shortcuts import render
import random
from paho.mqtt import client as mqtt


# Create your views here.

def connect(n : str, x : int):
    top = n
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(top)

    client = mqtt.Client(top)
    client.on_connect = on_connect
    client.connect("test.mosquitto.org", port=1883, keepalive=60)

    def on_publish(client, userdata, result):
        print("data published")
        pass

    client.on_publish = on_publish
    client.publish(topic=top, payload=x)

def index(request):
    return render(request, "projet/index.html")
def LED1(request):
    return render(request, "projet/LED1/LED1.html")
def LED1ON(request):
    connect(n="Courgette/banane/lièvre", x=1)
    return render(request, "projet/LED1/ON.html")
def LED1OFF(request):
    connect(n="Courgette/banane/lièvre", x=0)
    return render(request, "projet/LED1/OFF.html")
def LED2(request):
    return render(request, "projet/LED2/LED2.html")
def LED2ON(request):
    connect(n="Courgette/banane/lièvre2", x=1)
    return render(request, "projet/LED2/ON.html")
def LED2OFF(request):
    connect(n="Courgette/banane/lièvre2", x=0)
    return render(request, "projet/LED2/OFF.html")

