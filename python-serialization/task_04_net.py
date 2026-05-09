#!/usr/bin/env python3
""" Module for a Client-Server Application with Serialization"""

import socket
import json


def start_server():
    """function  that ets up a  server using the socket library"""
    host = ''
    port = 12345
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
    # accept() returns a NEW oscket
        conn, addr = s.accept()
        with conn:
            raw_data = conn.recv(1024)
            if raw_data:
                # Deserialize: Bytes -> String -> Dictionary
                data_dict = json.loads(raw_data.decode('utf-8'))
                print(f"Received Dictionary from Client:")
                print(data_dict)
    except (
            socket.error, socket.herroer, socket.gaierror,
            socket.timeout
    ) as err:
        raise err


def send_data(data_dict):
    """sends data"""
    host = 'localhost'
    port = 12345
    try:
        with socket.socket(socket.AF_INET,  socket.SOCK_STREAM) as s:
            s.connect((host, port))
            json_string = json.dumps(data_dict)
            s.sendall(json_string.encode('utf-8'))
    except (
            socket.error, socket.herroer, socket.gaierror,
            socket.timeout
    ) as err:
        raise err
