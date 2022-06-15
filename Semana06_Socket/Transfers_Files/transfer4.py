import socket
import select

UDP_IP = "127.0.0.1"                # Define o host UDP
IN_PORT = 5005                      # Define a porta UDP
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # inicializa um socket no protocolo UDP
sock.bind((UDP_IP, IN_PORT))                                # define o socket como um servidor

while True:
    data, addr = sock.recvfrom(1024)                        # recebe os dados do client no protocolo UDP
    if data:
        print ("File name:", data)
        file_name = data.strip()

    f = open(file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)               # recebe os dados do client no protocolo UDP
            f.write(data)
        else:
            print ("%s Finish!" % file_name)
            f.close()
            break