from server import CHUNK_SIZE
import socket
import pickle

CLIENT = socket.gethostname()
PORT = 1235                           #ports until 1233 might need admin on some devices 
ADDR = (CLIENT, PORT)


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)


CHUNK_SIZE = 1024 


def insertion():
    func = "I".encode('utf-8')
    client.send(func)
    print("Insert record")
    print("Enter values to be inserted: ")
    print("Date(dd-mm-yyyy): ", end=" ")
    date = input()
    print("foodid: ",end=" ")
    id = input()
    print("Quantity: ", end=" ")
    qty = int(input())
    print("Cost: ",end=" ")
    cost = int(input())

    insert_data = {'Date': date, 'foodid': id, 'Quantity' : qty,'Cost' : cost}

    msg = pickle.dumps(insert_data)
    msg = bytes(f"{len(msg):<{CHUNK_SIZE}}", 'utf-8')+msg
    status = client.send(msg)
    print("Status of sending: ",status)



def modification():
    message = 'M'.encode('utf-8')
    client.send(message)



def view():
    func = "V".encode('utf-8')
    client.send(func)
    message = 'View'.encode('utf-8')
    client.send(message)
    msg = {}
    client.recv(msg)
    recd = pickle.loads(msg)
    print(recd)



def update():
    func = "U".encode('utf-8')
    status = client.send(func)
    print("Status of sending: ",status)




cont = "Y"

while True and cont=="Y":
    print("Choose what you want to do: ")
    print("1. Insertion (I)")
    print("2. Modification (M)")
    print("3. View (V)")
    print("4. Update (U)")
    print("5. Display (F)")
    print("Type the appropriate option: ",close=" ")
    choice = input()

    if choice == 'I':
        insertion()

    elif choice == 'M':
        modification()

    elif choice == 'V':
        view()

    elif choice == 'U':
        update()

    else:
        print("Try again, invalid input")

    print("Do you want to continue? (Y/N) ", end="")
    cont = input()