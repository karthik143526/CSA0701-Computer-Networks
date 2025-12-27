# Function to perform XOR for CRC
def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

# Function to perform CRC division
def crc(data, key):
    n = len(key)
    temp = data[:n]

    while n < len(data):
        if temp[0] == '1':
            temp = xor(key, temp) + data[n]
        else:
            temp = xor('0'*n, temp) + data[n]
        n += 1

    if temp[0] == '1':
        temp = xor(key, temp)
    else:
        temp = xor('0'*len(key), temp)
    return temp

# ---------------- MAIN ----------------
data = input("Enter binary data: ")
key = input("Enter CRC key: ")

# Append zeros to data
appended_data = data + '0'*(len(key)-1)

# Calculate CRC remainder
remainder = crc(appended_data, key)
print("CRC Remainder / Checksum:", remainder)

# Transmitted data (data + remainder)
transmitted = data + remainder
print("Transmitted Data:", transmitted)

# ---------------- RECEIVER ----------------
received_data = transmitted  # You can simulate error by changing a bit
check = crc(received_data, key)

if '1' in check:
    print("Error detected in received data!")
else:
    print("No error detected. Data received successfully.")
