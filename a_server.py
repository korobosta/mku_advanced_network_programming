import socket

# Server configuration
HOST = '127.0.0.1'  # Loopback address
PORT = 65432  # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen()
    print('Server is listening for connections...')
    
    # Accept a new connection
    conn, addr = server_socket.accept()
    with conn:
        print(f'Connected by {addr}')
        
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            
            # Send the received data back to the client
            conn.sendall(data)
