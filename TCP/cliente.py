import socket

# Configurações de conexão
server_ip = '127.0.0.1' 
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))
print(f"Conectado ao servidor em {server_ip}:{server_port}")

while True:
    message = input("Sua mensagem para o servidor (ou 'sair' para sair): ")
    client_socket.send(message.encode('utf-8'))
    if message.lower() == 'sair':
        break
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Servidor diz: {data}")

client_socket.close()
