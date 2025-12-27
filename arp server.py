# arp_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8888))

arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03"
}

print("ARP Server is running...")

while True:
    ip, addr = server.recvfrom(1024)
    ip = ip.decode()
    print("ARP Request for IP:", ip)

    mac = arp_table.get(ip, "MAC Address not found")
    server.sendto(mac.encode(), addr)
