import pickle
import socket
import pandas as pd


PORT = 1234
SERVER = socket.gethostname()
ADDR = (SERVER,PORT)
CHUNK_SIZE = 1024



ListItems = pd.read_csv("FoodBill.csv")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


server.listen()
print('Server starting up.')
print('Server address: ',ADDR)

def insertion():
    data = server.recv(CHUNK_SIZE).decode('utf-8')
    recd = pickle.loads(data)
    print("Values recieved: ")
    print(recd)
    insert_row = list(recd.values())
    ListItems = ListItems.append(insert_row, ignore_index=True)


def view():
    print(ListItems)
    client.sendall(ListItems.to_string().encode("utf-8"))

def update():
    rows = len(ListItems.axes[0])
    for index in rows:
        id = ListItems.iloc[index]["foodid"]
        search_id = id[0]

        if search_id == "I":
            ChangedValue = "Italian"

        elif search_id == "D":
            ChangedValue = "Dosa"

        elif search_id == "A":
            ChangedValue = "Apple"

        else:
            ChangedValue = "Briyani"    
            
        ListItems.iloc[index]["Category"] = ChangedValue

        

def modify():
    rows = len(ListItems.axes[0])
    for index in rows:
        ChangedValue = ListItems.iloc[index]["Quantity"]*ListItems.iloc[index]["cost"]
        ListItems.iloc[index]["Totalcost"] = ChangedValue
    print("Updated")
    return



while True: 
    client,addr = server.accept()
    print(f'New connection established with {addr}')

    inp = (client.recv(CHUNK_SIZE).decode('utf-8'))
    if(inp=="I"):
        insertion()
    
    elif(inp=="M"):
        modify()

    elif(inp=="V"):
        view()

    elif(inp=="U"):
        update()

    





