# dns_client.py
import socket

# Read hostname from user
hostname = input("Enter hostname: ")

try:
    # Contact DNS server and resolve hostname
    ip_address = socket.gethostbyname(hostname)

    print("Hostname:", hostname)
    print("IP Address:", ip_address)

except socket.gaierror:
    print("Hostname could not be resolved")
