import socket
import random

HOST = 'localhost'  # Endereço IP do servidor
PORT = 3001  # Porta usada para a conexão

def NumeroAleatorio():
    return random.randint(1, 9)

# Configurando Socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

#Logica
N = 1
while N < 100:
    delta = NumeroAleatorio()
    N += delta
    print(f'Enviando o número {N}...')

    # Converte o número para um array de bytes
    data = N.to_bytes(4, byteorder='big')

    # Envia o dado para o servidor
    cliente.send(data)

    # Recebe o dado enviado pelo servidor
    dados = cliente.recv(1)  # recebe 4 bytes do servidor
    result = int.from_bytes(dados, byteorder='big')  # converte os bytes em inteiro usando ordem big-endian
    if result == 1:
        print(f'{N} é primo')
        print(f'...')
    elif result == 0:
        print(f'{N} não é primo')
        print(f'...')
    else:
        print(f'Erro o valor recebido foi: {result} existe uma falha no código do servidor')



# Fecha a conexão com o servidor
cliente.close()
