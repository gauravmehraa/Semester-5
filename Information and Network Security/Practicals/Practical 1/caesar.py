def encrypt(plaintext):
  ciphertext = ""
  for char in plaintext.upper():
    newchar = (ord(char) - ord('A') + 3) % 26
    ciphertext += chr(newchar + ord('A'))
  return ciphertext

def decrypt(ciphertext):
  plaintext = ""
  for char in ciphertext.upper():
    newchar = (26 + ord(char) - ord('A') - 3) % 26
    plaintext += chr(newchar + ord('A'))
  return plaintext

text = input("Enter message: ")
c = encrypt(text)
d = decrypt(c)
print(f"Ciphertext: {c}")
print(f"Plaintext: {d}")