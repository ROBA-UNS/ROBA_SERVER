import os
import datetime
import socket
import sys

import paho.mqtt.client as mqtt

# get ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_server = s.getsockname()[0]
s.close()

# This is the Server
nama_topik = "roba_uns_" + str(ip_server)
print(nama_topik)
un = "roba_uns"
passw = "roba123"
port = 1883

def status_rc(rc):
    if rc == 0:
        pesan_rc = "sukses"
    if rc == 1:
        pesan_rc = "connection refused - invalid protocol version"
    if rc == 2:
        pesan_rc = "connection refused - invalid client identifier"
    if rc == 3:
        pesan_rc = "connection refused - server unavailable"
    if rc == 4:
        pesan_rc = "connection refused - bad username or password"
    if rc == 5:
        pesan_rc = "connection refused - not authorized"
    return pesan_rc

def on_connect(client, userdata, flags, rc):
    print("Koneksi : " + status_rc(rc))
    print("Melakukan subscribe ke " + nama_topik)
    client.subscribe(nama_topik)

def on_message(client, userdata, msg):
    #print(msg)
    print("Pesan dari {}:".format(ip_server))
    print("{}".format(msg.payload.decode()))
    
client = mqtt.Client()
client.username_pw_set(username=un,password=passw)

while True:
    client.connect(ip_server,port,60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()