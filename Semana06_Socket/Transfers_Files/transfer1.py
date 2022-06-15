import socket   #   importa a biblioteca socket
import sys      #   importa a biblioteca sys

TCP_IP = "127.0.0.1"    #   define a variável host  
FILE_PORT = 5005        #   especifica a porta para o nome do arquivo
DATA_PORT = 5006        #   especifica a porta para os dados do arquivo
buf = 1024              #   num de bytes que será enviado

file_name = sys.argv[1] #   especifica o arquivo


try:                    #   tenta executar o código
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # inicializa um socket
    sock.connect((TCP_IP, FILE_PORT))    # conecta o socket no host e porta especificados
    sock.send(file_name)                 # envia o nome do arquivo para o servidor
    sock.close()                         # fecha o socket

    print ("Sending %s ..." % file_name) # imprime os status do programa

    f = open(file_name, "rb")            # abre um arquivo no modo de leitura em binário
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # inicializa um socket
    sock.connect((TCP_IP, DATA_PORT))    # conecta o socket no host e porta especificados
    data = f.read()                      # lê o arquivo aberto
    sock.send(data)                      # envia o arquivo lido para o servidor

finally:                # após executar o código
    sock.close()        # fecha o socket
    f.close()           # fecha o arquivo