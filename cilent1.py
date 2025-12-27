import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(('127.0.0.1', 7000))
print("Connected to chat server")

while True:
    # Send message to server
    msg = input("Client: ")
    client.send(msg.encode())

    if msg.lower() == "exit":
        break

    # Receive reply from server
    reply = client.recv(1024)

    # If server closes connection
    if not reply:
        print("Server disconnected")
        break

    print("Server:", reply.decode())

    if reply.decode().lower() == "exit":
        break

# Close connection
client.close()
print("Client closed")
