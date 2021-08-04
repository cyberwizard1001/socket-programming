import socket

PORT = 1234
SERVER = socket.gethostname()
ADDR = (SERVER,PORT)

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

while True:
    msg = input('Message to be sent to the server: ')
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        break