import socket
import threading


HEADER = 64
PORT = 5050
# SERVER = "192.168.12.9"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT_MESSAGE = "!DISCONECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[--NEW CONNECTION] {addr} conencted. \n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f'--[{addr}]: {msg}')
            conn.send("Message received".encode(FORMAT))
            
            if msg == DISCONECT_MESSAGE:
                connected = False
                print(f'--[{addr}] is disconected.')
        
            
     
    conn.close()


def start():
    server.listen()
    print(f"[--LISTENING] server is listening {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[--ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()