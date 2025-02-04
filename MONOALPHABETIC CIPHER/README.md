# Monoalphabetic Cipher Encryption  

## Introduction  
This script implements a **Monoalphabetic Cipher**, a type of substitution cipher where each letter in the plaintext is replaced with a corresponding letter from a user-defined replacement alphabet. This provides more security than the **Caesar Cipher** since each letter has a unique mapping instead of a fixed shift.  

## Features  
- Allows the user to define a custom 26-letter replacement alphabet.  
- Encrypts lowercase letters while keeping non-alphabetic characters unchanged.  
- Simple and efficient implementation for basic encryption.  

## How It Works  
1. **User Input:**  
   - The user provides a 26-character replacement alphabet (unique and in lowercase).  
   - The user enters the plaintext string to encrypt.  
2. **Letter Substitution:**  
   - Each letter in the plaintext is replaced based on its index in the original alphabet.  
   - Non-alphabetic characters remain unchanged.  
3. **Output:**  
   - The encrypted text (ciphertext) is displayed.  

## Usage  
### Running the Script  
1. Ensure you have Python installed.  
2. Copy the script into a Python file (e.g., `monoalphabetic_cipher.py`).  
3. Run the script using:  
   ```bash  
   python3 monoalphabetic_cipher.py  
   ```  
4. Enter the replacement alphabet and plaintext when prompted.  

### Example  
#### Input:  
```
Enter the replacement alphabet (26 unique letters): qwertyuiopasdfghjklzxcvbnm  
Enter the string you want to encrypt: hello  
```  
#### Output:  
```
Ciphertext: itssg  
```  
![SmartSelect_20250204_125609_M365 Copilot.jpg](https://github.com/user-attachments/assets/e46cac66-c00c-4e8c-9deb-79bb222aaa7e)



## Limitations  
- The replacement alphabet must contain **exactly 26 unique lowercase letters**.  
- Only lowercase letters are encrypted (uppercase letters remain unchanged).  

## License  
This script is open-source and can be used for educational purposes.