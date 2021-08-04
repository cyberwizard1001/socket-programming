import socket 

SERVER = socket.gethostname()
PORT = 1234
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)

server.listen(7)
print("Server started")

while True:
    client,addr = server.accept()
    print('New connectionL: {addr}')

    message = 'Thanks for connecting!'.encode('utf-8')
    client.send(message)

    print("Server shutting down")

    client.close()