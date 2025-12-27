import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

domain = input("Enter domain name: ")
client.sendto(domain.encode(), ('127.0.0.1', 9999))

ip, _ = client.recvfrom(1024)
print("IP Address:", ip.decode())

client.close()