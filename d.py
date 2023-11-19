import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket to non-blocking mode
sock.setblocking(False)