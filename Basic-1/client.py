# Basic client program to connect to server and receive messages and display them

import socket

# Define address and hostname of server to connect
SERVER = socket.gethostname()
PORT = 1234                           #ports until 1233 might need admin on some devices 
ADDR = (SERVER, PORT)

# Initialize a socket object, connectionless - TCP - SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        #IPV4, TCP - TCP/IP connection

# Connect to server
client.connect(ADDR)              
#server would bind itself to a host and port, client connects to a server program bound to the host and port entered here


# Receive message:
CHUNK_SIZE = 4 # 4 Bytes
while True:
    msg = client.recv(CHUNK_SIZE).decode('utf-8')
    if len(msg) <= 0:
        break
    print(msg)

print('Client received all data...')