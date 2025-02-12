import numpy as np
import math
import hashlib

# --------------------------- PLAYFAIR CIPHER ---------------------------
def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I").replace(" ", "")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key += "".join(c for c in alphabet if c not in key)
    return np.array(list(key)).reshape(5, 5)

def find_position(matrix, letter):
    row, col = np.where(matrix == letter)
    return row[0], col[0]

def playfair_encrypt(text, matrix):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    encrypted_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            encrypted_text += matrix[row_a, (col_a + 1) % 5] + matrix[row_b, (col_b + 1) % 5]
        elif col_a == col_b:
            encrypted_text += matrix[(row_a + 1) % 5, col_a] + matrix[(row_b + 1) % 5, col_b]
        else:
            encrypted_text += matrix[row_a, col_b] + matrix[row_b, col_a]
    return encrypted_text

def playfair_decrypt(text, matrix):
    decrypted_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            decrypted_text += matrix[row_a, (col_a - 1) % 5] + matrix[row_b, (col_b - 1) % 5]
        elif col_a == col_b:
            decrypted_text += matrix[(row_a - 1) % 5, col_a] + matrix[(row_b - 1) % 5, col_b]
        else:
            decrypted_text += matrix[row_a, col_b] + matrix[row_b, col_a]
    return decrypted_text.rstrip('X')

# --------------------------- COLUMNAR TRANSPOSITION ---------------------------
def columnar_encrypt(text, key):
    key_hash = hashlib.sha256(key.encode()).hexdigest()[:len(key)]
    sorted_key = sorted(range(len(key_hash)), key=lambda k: key_hash[k])
    num_cols = len(sorted_key)
    num_rows = math.ceil(len(text) / num_cols)
    text += 'X' * (num_rows * num_cols - len(text))
    matrix = [list(text[i:i+num_cols]) for i in range(0, len(text), num_cols)]
    return "".join("".join(matrix[row][col] for row in range(num_rows)) for col in sorted_key)

def columnar_decrypt(text, key):
    key_hash = hashlib.sha256(key.encode()).hexdigest()[:len(key)]
    sorted_key = sorted(range(len(key_hash)), key=lambda k: key_hash[k])
    num_cols = len(sorted_key)
    num_rows = len(text) // num_cols
    matrix = [[''] * num_cols for _ in range(num_rows)]
    index = 0
    for col in sorted_key:
        for row in range(num_rows):
            matrix[row][col] = text[index]
            index += 1
    return "".join("".join(row) for row in matrix).rstrip('X')

# --------------------------- HYBRID CIPHER ---------------------------
def hybrid_encrypt(plaintext, playfair_key, columnar_key):
    playfair_matrix = generate_playfair_matrix(playfair_key)
    playfair_ciphertext = playfair_encrypt(plaintext, playfair_matrix)
    return columnar_encrypt(playfair_ciphertext, columnar_key)

def hybrid_decrypt(ciphertext, playfair_key, columnar_key):
    playfair_matrix = generate_playfair_matrix(playfair_key)
    playfair_ciphertext = columnar_decrypt(ciphertext, columnar_key)
    return playfair_decrypt(playfair_ciphertext, playfair_matrix)

# User Input
plaintext = input("Enter the plaintext: ")
playfair_key = input("Enter the Playfair cipher key: ")
columnar_key = input("Enter the Columnar Transposition cipher key: ")

encrypted_text = hybrid_encrypt(plaintext, playfair_key, columnar_key)
decrypted_text = hybrid_decrypt(encrypted_text, playfair_key, columnar_key)

print("\nPlaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)