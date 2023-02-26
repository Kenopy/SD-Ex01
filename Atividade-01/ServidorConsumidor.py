import socket
import math

HOST = ''  # Endereço IP do servidor
PORT = 3001  # Porta que o servidor vai escutar

# Cria um objeto socket do tipo TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind do socket com o endereço e porta especificados
server_socket.bind((HOST, PORT))

# Fica aguardando conexões
server_socket.listen(1)

print(f"Aguardando conexões na porta {PORT}...")



while True:
    # Aceita uma nova conexão
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")
    
    # Lê dados enviados pelo cliente
    dadosCliente = client_socket.recv(4)

    N= int.from_bytes(dadosCliente, byteorder='big')
    
    print(f"Recebido: {N}")
    

    cont = 1
    for i in range(2, N):
        if N % i == 0:
            cont += 1
    if cont <= 1:
        print ('Erro no codigo')
    elif cont == 2:
        result = 1
    else:
        result = 0

    
    
    # Envia resultado de volta para o cliente
    numero_bytes = result.to_bytes(4, byteorder='big')  # converte para 4 bytes usando ordem big-endian
    client_socket.send(numero_bytes)  # envia os bytes para o cliente
