import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 6000))

while True:
    msg = input("Enter message (type exit to stop): ")
    if msg.lower() == "exit":
        break

    client.send(msg.encode())
    data = client.recv(1024)
    print("Echo from server:", data.decode())

client.close()
