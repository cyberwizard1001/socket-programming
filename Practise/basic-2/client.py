import socket 

SERVER = socket.gethostname()
PORT = 1234
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

CHUNK_SIZE = 1024

while True:
    send_msg = input()
    client.send(send_msg.encode('utf-8'))

    if send_msg=='exit':
        break

    msg = client.recv(CHUNK_SIZE).decoded('utf-8')
    print('Server:',msg)

    print('Client recieved data...')