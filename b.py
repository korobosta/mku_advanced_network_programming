import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Loopback address
PORT = 65432  # Port to listen on

# Function to handle each client connection
def handle_client(client_socket, addr):
    print(f'Connected by {addr}')
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)  # Echo back the received data
    
    print(f'Connection with {addr} closed')
    client_socket.close()

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen()
    print('Server is listening for connections...')
    
    while True:
        # Accept a new connection
        client_socket, addr = server_socket.accept()
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()
