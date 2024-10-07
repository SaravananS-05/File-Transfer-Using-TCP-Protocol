import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5001))
server_socket.listen(5)
print("Server listening on port 5001...")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    filename = conn.recv(1024).decode()
    try:
        with open(filename, 'rb') as f:
            while chunk := f.read(1024):
                conn.sendall(chunk)
        print(f"File '{filename}' sent successfully.")
    except FileNotFoundError:
        conn.sendall(b'')
        print(f"File '{filename}' not found.")
    
    conn.close()
