def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def RSA(p, q, m):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break
    print("Considering e =", e)
    
    j = 0
    while True:
        if (j * e % phi) == 1:
            d = j
            break
        j += 1
    
    c = (m ** e) % n
    print("Encrypted =", c)
    
    d = (c ** d) % n
    print("Decrypted =", d)

# User input
p = int(input("Enter the value p: "))
q = int(input("Enter the value q: "))
m = int(input("Enter the message: "))

RSA(p, q, m)
