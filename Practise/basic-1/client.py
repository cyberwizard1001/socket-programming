import socket 

SERVER = socket.gethostname()       # returns hostname of host itself 
PORT = 1234
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

CHUNK_SIZE = 4 
while True:
    msg=client.recv(CHUNK_SIZE).decode('utf-8')
    if len(msg)<=0:
        break
    print(msg)

print("Client received data")