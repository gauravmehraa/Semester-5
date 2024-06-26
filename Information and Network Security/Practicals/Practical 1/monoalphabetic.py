def encrypt(plaintext, key):
  ciphertext = ""
  for char in plaintext.upper():
    if char == ' ': ciphertext += ' '
    else:
      newchar = (ord(char) - ord('A') + key) % 26
      ciphertext += chr(newchar + ord('A'))
  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ""
  for char in ciphertext.upper():
    if char == ' ': plaintext += ' '
    else:
      newchar = (26 + ord(char) - ord('A') - key) % 26
      plaintext += chr(newchar + ord('A'))
  return plaintext

text = input("Enter message: ")
key = int(input("Enter key: "))
if 0 >= key or key >= 26:
  print("Invalid key")
  exit()

c = encrypt(text, key)
d = decrypt(c, key)
print(f"Ciphertext: {c}")
print(f"Plaintext: {d}")