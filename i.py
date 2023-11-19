import socket

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket options for send buffer size
send_buffer_size = 4096  # Modify this value as needed
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, send_buffer_size)

# Set the socket options for receive buffer size
receive_buffer_size = 8192  # Modify this value as needed
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, receive_buffer_size)

# Get the current buffer sizes (optional, for verification)
current_send_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
current_receive_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
print(f"Current send buffer size: {current_send_buffer_size}")
print(f"Current receive buffer size: {current_receive_buffer_size}")

# Close the socket (optional)
sock.close()
