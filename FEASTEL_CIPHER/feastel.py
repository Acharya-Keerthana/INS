def string_to_binary(s):
    return "".join(format(ord(i), '08b') for i in s)

def feistel_encrypt_decrypt(s, key):
    # Convert input string to binary
    result = string_to_binary(s)
    
    # Split into left and right halves
    l = len(result) // 2
    left, right = result[:l], result[l:]

    # Convert key to binary
    key_bin = string_to_binary(key)

    # First round
    s = bin(int(right, 2) + int(key_bin, 2))[2:]
    answer = bin(int(s, 2) ^ int(left, 2))[2:]
    new_r = answer
    new_l = right

    # Swap
    new_r, new_l = new_l, new_r

    # Second round
    s = bin(int(new_r, 2) + int(key_bin, 2))[2:]
    ans = bin(int(s, 2) ^ int(new_l, 2))[2:]
    nl = new_r
    nr = ans
    nl, nr = nr, nl

    # Generate ciphertext
    cipher = nl + nr

    # Ensure length consistency
    while len(cipher) < len(result):
        cipher = "0" + cipher

    return cipher

def binary_to_string(binary_data):
    plain_text = ""
    for i in range(0, len(binary_data), 8):
        temp = binary_data[i:i+8]
        d = int(temp, 2)
        plain_text += chr(d)
    return plain_text

# Input from user
s = input("Enter a string: ")
key = input("Enter a key: ")

# Encryption
cipher_text = feistel_encrypt_decrypt(s, key)
print("Ciphertext (binary):", cipher_text)

# Convert binary to readable text
plain_text = binary_to_string(cipher_text)
print("Decrypted text:", plain_text)
