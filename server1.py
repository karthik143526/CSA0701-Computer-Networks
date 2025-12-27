import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 7000))
server.listen(1)

print("Chat Server is running... Waiting for client...")

conn, addr = server.accept()
print("Client connected:", addr)

while True:
    data = conn.recv(1024)

    # If client closes connection
    if not data:
        print("Client disconnected")
        break

    msg = data.decode()
    print("Client:", msg)

    if msg.lower() == "exit":
        print("Chat ended by client")
        break

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server.close()
print("Server closed")
