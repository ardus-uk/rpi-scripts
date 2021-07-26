#!/usr/bin/env python3
import socket
import json
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
jcf = os.path.join(script_directory, "servers.json")
with open(jcf) as json_credentials_file:
    credentials = json.load(json_credentials_file)

# Choose a server - could be u3apeter, dxantix, or markpi
server = 'u3apeter'

HOST = credentials[server]['host']
PORT = credentials[server]['port']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    input_prompt = 'Message text (leave blank to end the program) '
    while True:
        message=input(input_prompt)
        if message == '':
            break
        else:
            data_out=bytes(message,'utf-8')
            s.sendall(data_out)
            data_in = s.recv(1024)
            print('---- Sent ---- ', repr(data_out))
            print('-- Received -- ', repr(data_in))
