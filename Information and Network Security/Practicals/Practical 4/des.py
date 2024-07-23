def encrypt(plaintext, key):
    ciphertext = ''
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    return plaintext

text = input("Enter message: ")
key = input("Enter key: ")
e = encrypt(text, key)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")