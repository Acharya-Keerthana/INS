import numpy as np

def encrpt(plaintext,key_matrics):
    n=len(key_matrics) #for 3x3  n=3
    plaintext=plaintext.upper().replace(" ","")
    # addition of X at the end for uneven length
    if len(plaintext)%n!= 0:
        plaintext+= "X" * (n-len(plaintext)%n)
        
    plaintext_vector= [ord(char)-ord('A') for char in plaintext]
    ciphertext=" "
    for i in range(0,len(plaintext_vector),n):
        block=plaintext_vector[i:i+n]
        result=np.dot(key_matrics,block)%26 #dot means multiplication
        ciphertext+="".join(chr(num+ord('A'))for num in result)# chr is unicode for one char
    return ciphertext

print("Sample Example plaintext:HELLO and key_matrix:[[6, 24, 1], [13, 16, 10], [20, 17, 15]")
plaintext = "HELLO"
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  
print("Encrypted:", encrpt(plaintext, key_matrix))

plaintext = input("Enter the plaintext:")
key_matrix = np.array([[7,8], [11,11]])
print("Encrypted:", encrpt(plaintext, key_matrix))
