import socket

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP and Port
s.bind(('127.0.0.1', 5000))
s.listen(1)

print("Server waiting for connection...")

# Accept client connection
conn, addr = s.accept()
print("Connected to:", addr)

# Receive date and time from client
data = conn.recv(1024).decode()
print("Date and Time from Client:", data)

# Close connection
conn.close()
s.close()
