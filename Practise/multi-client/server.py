import socket 
import threading

PORT = 1234
SERVER = socket.gethostname()
ADDR = (SERVER,PORT)
DISCONNECT = '!DISCONNECT'
CHUNK_SIZE = 32
FORMAT = 'utf-8'


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(conn,addr):
    connected = True 
    while connected:
        msg = conn.recv(CHUNK_SIZE).decode(FORMAT)
        if len(msg)>0:
            if msg == DISCONNECT:
                connected = False
            print('[{addr}]:{msg}')

        conn.close()

def start():
    server.lsiten()
    print('[SERVER] Listening on:',ADDR)
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

print('[SERVER] Starting...')
start()