# Caesar Cipher Encryption  

## Introduction  
This script implements the **Caesar Cipher** encryption and decryption algorithm in Python. The **Caesar Cipher** is a simple shift cipher that replaces each letter in the plaintext with another letter a fixed number of positions down the alphabet.  

## Features  
- Encrypts both uppercase and lowercase letters.  
- Maintains non-alphabetic characters (spaces, punctuation, numbers) unchanged.  
- Supports user-defined shift values (key).  

## How It Works  
1. **Input Handling:**  
   - The user enters the plaintext and a numeric key (shift value).  
2. **Character Shifting:**  
   - Each letter is shifted forward by the key value.  
   - If the shift moves past 'Z' or 'z', it wraps around to the start of the alphabet.  
   - Uppercase and lowercase letters are handled separately.  
3. **Non-Letter Handling:**  
   - Non-alphabetic characters remain unchanged.  
4. **Output:**  
   - The encrypted ciphertext is displayed.  

## Usage  
### Running the Script  
1. Ensure Python is installed on your system.  
2. Copy the script into a Python file (e.g., `caesar_cipher.py`).  
3. Run the script using:  
   ```bash  
   python caesar_cipher.py  
   ```  
4. Enter the plaintext and key when prompted.  

OUTPUT

![SmartSelect_20250204_124302_Dropbox.jpg](https://github.com/user-attachments/assets/361107fe-cea9-48c5-ac17-4446741751df)

## Link to the codespace
/workspaces/INS/CEASES_CIPHER/ceasescipher.py

## License  
This script is open-source and can be used for educational purposes.
