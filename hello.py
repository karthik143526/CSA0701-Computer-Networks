# ================== TCP ECHO SERVER ==================
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 6000))
server.listen(1)

print("Echo Server is running...")

conn, addr = server.accept()
print("Connected to client:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received:", data.decode())
    conn.send(data)   # Echo back

conn.close()
server.close()


