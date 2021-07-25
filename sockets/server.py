#!/usr/bin/env python3
import socket
from datetime import datetime
# Listen from any host
HOST = ''
# Listen on the following port
PORT = 4472

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
