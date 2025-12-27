# file_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

# Receive file name first
file_name = conn.recv(1024).decode()
print("Receiving file:", file_name)

with open("received_" + file_name, "wb") as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

print("File received successfully")

conn.close()
server.close()
