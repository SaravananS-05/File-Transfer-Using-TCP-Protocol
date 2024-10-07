import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = sys.argv[1]
filename = sys.argv[2]

client_socket.connect((server_ip, 5001))

client_socket.sendall(filename.encode())

with open(f'downloaded_{filename}', 'wb') as f:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        f.write(data)

print(f"File '{filename}' downloaded successfully.")
client_socket.close()
