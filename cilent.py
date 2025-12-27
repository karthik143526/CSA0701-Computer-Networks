import socket
from datetime import datetime

# Create TCP socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
c.connect(('127.0.0.1', 5000))

# Get current date and time
dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Send date and time to server
c.send(dt.encode())
print("Sent Date and Time:", dt)

# Close connection
c.close()
