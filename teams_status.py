import paho.mqtt.client as mqtt
import blinkt
from subprocess import call

def status_busy():
  blinkt.clear()
  blinkt.set_all(255, 0, 0)
  blinkt.show()

def status_avail():
  blinkt.clear()
  blinkt.set_all(0, 255, 0)
  blinkt.show()

def status_away():
  blinkt.clear()
  blinkt.set_all(255, 165, 0)
  blinkt.show()

def status_locked():
  blinkt.clear()
  blinkt.show()

def status_shutdown():
  status_locked()
  call("sudo shutdown -h now", shell=True)

def on_message(client, userdata, message):
  print("Message Received ", str(message.payload.decode("utf-8")))
  message = message.payload.decode("utf-8")
  if message == "Busy":
    status_busy()
  elif message == "Away":
    status_away()
  elif message == "Available":
    status_avail()
  elif message == "Locked":
    status_locked()
  elif message == "Shutdown":
    status_shutdown()

#Assume Availiable
status_avail()

#Connect to MQTT
broker_address = "192.168.68.121"
client = mqtt.Client("Pi4")
client.on_message = on_message

client.connect(broker_address)
client.loop_start()

client.subscribe("/work/teams/status")

client.loop_forever()
