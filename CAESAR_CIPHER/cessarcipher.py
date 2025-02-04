original = "abcdefghijklmnopqrstuvwxyz"
replacement = input("Enter the replacement alphabet (26 unique letters): ")
inputtxt = input("Enter the string you want to encrypt: ")
Ciphertext = ""
for char in inputtxt:
    if char in original:
        Value = original.index(char)
        Ciphertext += replacement[Value]
    else:
        Ciphertext += char
print("Ciphertext:",Ciphertext)

inputtxt = input("Enter the string you want to decrypt: ")
Plaintext = ""
for char in inputtxt:
    if char in replacement:
        Value = replacement.index(char)
        Plaintext += original[Value]
    else:
        Plaintext += char
print("Plaintext:",Plaintext)