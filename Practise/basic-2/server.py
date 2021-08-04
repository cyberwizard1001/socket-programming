import socket 

SERVER = socket.gethostname()
PORT = 1234
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)

server.listen(ADDR)

server.listen(5)
print('Server started...')

client,addr = server.accept()
while True:
    print('New connection: {addr}')

    recv_msg = client.recv(1024).decode('utf-8')

    if recv_msg=='exit':
        client.close()
        break

    if recv_msg=='ping':
        message = 'pong!!!'.encode('utf-8')

    else:
        message = recv_msg.encode('utf-8')

    client.send(message)

print('Server shutting down...')