def encrypt(plaintext):
  return

def decrypt(ciphertext):
  return

key = input("Enter keyword: ").upper()
text = input("Enter message: ")
e = encrypt(text, key)
print(f"Encrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")