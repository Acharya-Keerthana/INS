def encrypt_func(plaintext, key):  
    Ciphertext = ""  # Initialize the ciphertext string
   
    for i in range(len(plaintext)):
        char=plaintext[i] 
        if char.isalpha():  # Check if the character is a letter
            if char.isupper():
                value = 65
            else:
                value = 97  
            Ciphertext += chr((ord(char) - value + key) % 26 + value)  
        else:
            Ciphertext += char  
            
    return Ciphertext 

plaintext = input("Enter the plain text: ")
key = int(input("Enter the key: ")) 

print("Ciphertext: " + encrypt_func(plaintext, key))

def decrypt_func(ciphertext, key):  
    Plaintext = ""  # Initialize the plaintext string
   
    for i in range(len(ciphertext)):
        char=ciphertext[i]   
        if char.isalpha():  # Check if the character is a letter
            # Calculate base ASCII value (65 for uppercase, 97 for lowercase)
            if char.isupper():
                value = 65
            else:
                value = 97  
            # Shift the character back and wrap around
            Plaintext += chr((ord(char) - value - key) % 26 + value)  
        else:
            # Append non-alphabetic characters as-is
            Plaintext += char  
            
    return Plaintext  


ciphertext = input("Enter the cipher text: ")
key = int(input("Enter the key: "))

print("Plaintext: " + decrypt_func(ciphertext, key))
