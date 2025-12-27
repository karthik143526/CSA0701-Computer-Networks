# file_client.py
import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

# Specify file to send
file_name = "send_file.txt"

if not os.path.exists(file_name):
    print("File not found!")
    client.close()
    exit()

# Send file name first
client.send(file_name.encode())

# Send file data
with open(file_name, "rb") as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client.send(data)

print("File sent successfully")
client.close()
