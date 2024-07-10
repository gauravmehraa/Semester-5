def displayMatrix(grid):
  for i in range(26):
    for j in range(26):
      print(grid[i][j], end = ' ')
    print()

def getMatrix():
  letters = [chr(x) for x in range(65, 91)]
  grid = [['_' for _ in range(26)] for _ in range(26)]
  start = 0
  for row in range(26):
    ptr = start
    for col in range(26):
      grid[row][col] = letters[ptr]
      ptr = (ptr + 1) % 26
    start += 1
  return grid

def padKey(text, key):
  newkey = ''
  n = len(key)
  ptr = 0
  for _ in text:
    newkey += key[ptr]
    ptr = (ptr + 1) % n
  return newkey


def encrypt(plaintext, key):
  plaintext = plaintext.upper()
  grid = getMatrix()
  key = padKey(plaintext, key)
  ciphertext = ''
  for i in range(len(plaintext)):
    if plaintext[i] == ' ': continue
    row = ord(key[i]) - ord('A')
    col = ord(plaintext[i]) - ord('A')
    ciphertext += grid[row][col]
  return ciphertext

def decrypt(ciphertext, key):
  ciphertext = ciphertext.upper()
  grid = getMatrix()
  key = padKey(ciphertext, key)
  plaintext = ''
  for i in range(len(ciphertext)):
    row = ord(key[i]) - ord('A')
    for j in range(26):
      if grid[row][j] == ciphertext[i]:
        plaintext += chr(j + ord('A'))
        break
  return plaintext

text = input("Enter message: ")
key = input("Enter keyword: ").upper()
if len(key) > len(text):
  print("Invalid key")
  exit()
e = encrypt(text, key)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")