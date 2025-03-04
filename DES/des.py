import random

s = input("Enter the string: ")

# Convert string to binary representation
result = ''.join(format(ord(i), '08b') for i in s)
answer = ""

# Remove every 8th bit
for i in range(len(result)):
    if i % 8 != 0:
        answer += result[i]

# Split binary string into two halves
l = int(len(answer) / 2)
left = answer[:l]
right = answer[l:]

# Shift values for transformations
lt = [2, 3, 6, 7, 1, 6, 5, 9]

keys = []

# Key generation process
for i in range(8):
    newKey = ""
    newAnswer = ""

    # Convert binary strings to integers, perform bitwise shift
    nl = int(left, 2)
    nl = bin(nl << lt[i])
    num = 2 + lt[i]

    nr = int(right, 2)
    nr = bin(nr << lt[i])

    # Create new key by combining shifted parts
    newKey = nr[num:] + nl[num:]

    # Random selection for obfuscation
    rm = []
    while len(rm) != 8:
        r = random.randint(0, len(newKey) - 1)  # Fixed: 'randit' to 'randint'
        if r not in rm:
            rm.append(r)

    # Create the final key
    for i in range(len(newKey)):
        if i not in rm:
            newAnswer += newKey[i]

    keys.append(newAnswer)

# Print generated keys
for i in range(len(keys)):
    print("Key", i + 1, "=", keys[i])
