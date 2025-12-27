# Bit Stuffing without recursion

data = input("Enter binary data: ")

count = 0
stuffed = ""

# -------- BIT STUFFING --------
for bit in data:
    if bit == '1':
        count += 1
        stuffed += bit
        if count == 5:
            stuffed += '0'   # Stuff 0 after five 1s
            count = 0
    else:
        stuffed += bit
        count = 0

print("Stuffed Data:", stuffed)


# -------- BIT DE-STUFFING --------
count = 0
destuffed = ""
i = 0

while i < len(stuffed):
    if stuffed[i] == '1':
        count += 1
        destuffed += stuffed[i]
        if count == 5:
            i += 1   # Skip stuffed 0
            count = 0
    else:
        destuffed += stuffed[i]
        count = 0
    i += 1

print("De-Stuffed Data:", destuffed)
