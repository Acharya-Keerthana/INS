def create_playfair_matrix(key): 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is excluded
    matrix = []
    key = "".join(dict.fromkeys(key.upper().replace("J", "I") + alphabet))  # Unique characters

    for i in range(0, 25, 5):
        matrix.append(list(key[i:i+5]))

    return matrix


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")

    if len(plaintext) % 2 != 0:
        plaintext += "X"  # Padding for odd length

    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


# Example usage
plaintext = input("Enter the string you want to encrypt: ")
key = input("Enter the keyword ")
print("Encrypted:", playfair_encrypt(plaintext, key))

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext


# Example usage
ciphertext = input("Enter the string you want to decrypt: ")
key = input("Enter the keyword: ")
print("Decrypted:", playfair_decrypt(ciphertext, key))


