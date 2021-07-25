#!/usr/bin/env python3
import socket
import json
import os

from datetime import datetime

script_directory = os.path.dirname(os.path.abspath(__file__))
jcf = os.path.join(script_directory, "config_server.json")
with open(jcf) as json_credentials_file:
    credentials = json.load(json_credentials_file)

# Choose a server - could be u3apeter, dxantix, or markpi
server = 'u3apeter'

# Listen from any host
HOST = ''
# Listen on the following port
PORT = credentials['port']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr, 'at', datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('Received: ',repr(data), 'at', datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
                conn.sendall(data)
