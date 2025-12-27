import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))

dns_table = {
    "google.com": "142.250.72.14",
    "yahoo.com": "98.137.11.163",
    "localhost": "127.0.0.1"
}

print("DNS Server is running...")

data, addr = server.recvfrom(1024)
domain = data.decode()

ip = dns_table.get(domain, "Domain not found")

server.sendto(ip.encode(), addr)
server.close()
