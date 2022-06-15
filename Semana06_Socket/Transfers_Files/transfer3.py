import socket
import time
import sys

UDP_IP = "127.0.0.1"                # Define o host UDP
UDP_PORT = 5005                     # Define a porta UDP
buf = 1024
file_name = sys.argv[1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(file_name, (UDP_IP, UDP_PORT))      # envia um nome de arquivo em pacotes UDP
print ("Sending %s ..." % file_name)
f = open(file_name, "r")
data = f.read(buf)
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):      # envia o conteúdo do arquivo em pacotes UDP
        data = f.read(buf)
        time.sleep(0.02) 

sock.close()
f.close()