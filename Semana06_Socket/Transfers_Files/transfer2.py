import socket      #   importa a biblioteca socket

TCP_IP = "127.0.0.1"    #   define a variável host
FILE_PORT = 5005        #   especifica a porta para o nome do arquivo
DATA_PORT = 5006        #   especifica a porta para os dados do arquivo
timeout = 3             #   cria uma variável aleatória que não é utilizada
buf = 1024              #   num de bytes que será recebido


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inicializa um socket
sock_f.bind((TCP_IP, FILE_PORT))        # transforma o socket em um servidor e inicializa com o host e a porta de arquivo
sock_f.listen(1)                        # cria uma tentativa de conexão com no máximo 1 client

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inicializa outro socket
sock_d.bind((TCP_IP, DATA_PORT))         # transforma o socket em um servidor e inicializa com o host e a porta de dados
sock_d.listen(1)                         # cria uma tentativa de conexão com no máximo 1 client


while True:                             # cria um loop
    conn, addr = sock_f.accept()        # conecta com o client 
    data = conn.recv(buf)               # recebe o nome do arquivo de até o numero de bytes especificado
    if data:                            # caso tenha recebido algo
        print ("File name:", data)      # mostra o nome do arquivo
        file_name = data.strip()        # remove os espaços no começo e final do nome do arquivo

    f = open(file_name, 'wb')           # abre ou cria um arquivo no modo de escrita em binário

    conn, addr = sock_d.accept()        # conecta com o client
    while True:                         # cria um loop
        data = conn.recv(buf)           # recebe uma quantidade buf de dados do client
        if not data:                    # caso nao receba nada
            break                       # sai do loop
        f.write(data)                   # escreve no arquivo aberto o que o client enviou

    print("%s Finish!" % file_name)     # mostra os status do programa
    f.close()                           # fecha o arquivo