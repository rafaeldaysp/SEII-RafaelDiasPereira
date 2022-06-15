from ast import arg
import threading
import socket

HEADER = 64
PORT = 5050
SERVER = '192.168.56.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT_MESSAGE = "!DISCONECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    send_length = str(len(message)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    retorno = client.recv(50)
    print(retorno.decode(FORMAT))


while True:
    msg = input()
    send(msg)
