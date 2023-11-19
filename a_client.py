import socket

# Server configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 65432  # Port used by the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    
    # Send data to the server
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())
    
    # Receive data from the server
    data = client_socket.recv(1024)
    print('Received:', data.decode())
