# arp_client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter IP address to find MAC: ")

client.sendto(ip.encode(), ('127.0.0.1', 8888))

mac, _ = client.recvfrom(1024)
print("MAC Address:", mac.decode())

client.close()
