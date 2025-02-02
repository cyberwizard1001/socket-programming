import pickle
import socket
import pandas as pd


PORT = 1234
SERVER = socket.gethostname()
ADDR = (SERVER,PORT)
CHUNK_SIZE = 1024

FORMAT = 'utf-8'

ListItems = pd.read_csv("FoodBill.csv")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


server.listen()
print('Server starting up.')
print('Server address: ',ADDR)

def insertion():
    return


def view():
    return

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
    return
    


while True: 
    client,addr = server.accept()
    print(f'New connection established with {addr}')

    inp = (client.recv(CHUNK_SIZE).decode('utf-8'))
    if(inp=="I"):
        data = client.recv(CHUNK_SIZE)
        recd = pickle.loads(data)
        print("Values recieved: ")
        print(recd)
        insert_row = list(recd.values())
        ListItems = ListItems.append(insert_row, ignore_index=True)
    
    elif(inp=="M"):
        rows = len(ListItems.axes[0])
        for index in rows:
            ChangedValue = int(ListItems.iloc[index]["Quantity"])*int(ListItems.iloc[index]["cost"])
            ListItems.iloc[index]["Totalcost"] = ChangedValue
        print("Updated")

    elif(inp=="V"):
        view()

    elif(inp=="U"):
        update()

    





