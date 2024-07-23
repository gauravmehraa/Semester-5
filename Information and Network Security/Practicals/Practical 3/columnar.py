import math

def getSequence(key):
  sortedkey = sorted(key)
  sequence = [sortedkey.index(char) for char in key]
  return sequence

def encrypt(plaintext, key):
  ciphertext = ''
  sequence = getSequence(key)
  rows = math.ceil(len(plaintext) / len(key))
  cols = len(key)
  matrix = [['_' for _ in range(cols)] for _ in range(rows)]

  index = 0
  for i in range(rows):
    for j in range(cols):
      if index >= len(plaintext): continue
      matrix[i][j] = plaintext[index]
      index += 1
  
  for _ in range(len(key)):
    index = sequence.index(min(sequence)) # find index of smallest number
    for row in matrix:
      ciphertext += row[index]
      del row[index] # remove element once added to CT
    sequence.remove(min(sequence)) # remove smallest number

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