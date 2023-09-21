import socket

# Configurações do servidor, não importa qual, desde que o cliente saiba o IP e a PORTA
host = '127.0.0.1' 
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen(1)
print(f"Servidor ouvindo em {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Conexão estabelecida com {client_address}")

while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"\nCliente -> {data}\n")
    response = input("\nSua resposta: ")
    client_socket.send(response.encode('utf-8'))

# Tudo que abre tem que ser fechado
client_socket.close()
server_socket.close()
