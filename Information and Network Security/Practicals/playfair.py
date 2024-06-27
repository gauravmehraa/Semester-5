def getKeyword(keyword):
  key = ""
  chars = set()
  for char in keyword:
    if char not in chars: key += char
    chars.add(char)
  return key

def getMatrix(keyword):
  key = getKeyword(keyword)
  keyset = set(key)
  grid = [['_' for _ in range(5)] for _ in range(5)]
  ptr = 0
  letter = 65

  # Fill word
  for row in range(5):
    for col in range(5):
      if key[ptr] == letter: letter += 1
      grid[row][col] = key[ptr]
      ptr += 1
      if ptr >= len(key): break
    if ptr >= len(key): break

  # Fill remaining letters
  for row in range(5):
    for col in range(5):
      if grid[row][col] != '_': continue
      while chr(letter) in keyset: letter += 1
      if letter == 73:
        grid[row][col] = 'I/J'
        letter += 1
      else:
        grid[row][col] = chr(letter)
      letter += 1
  return grid

def getPairs(text):
  pairs = []
  text = list(text)
  l = len(text)
  i = 0
  while i < l:
    if i == l - 1:
      pairs.append(f'{text[i]}X')
      break
    if text[i] == text[i+1]:
      pairs.append(f'{text[i]}X')
      text.insert(i+1, 'X')
      l += 1
    else:
      pairs.append(f'{text[i]}{text[i+1]}')
    i += 2
  return pairs

def getPositions(grid):
  positions = {}
  for row in range(5):
    for col in range(5):
      positions[grid[row][col]] = [row, col]
  return positions

def encrypt(plaintext, key):
  grid = getMatrix(key)
  pairs = getPairs(plaintext.upper())
  positions = getPositions(grid)
  ciphertext = ""
  for pair in pairs:
    [row1, col1] = positions[pair[0]] if pair[0] not in 'IJ' else positions['I/J']
    [row2, col2] = positions[pair[1]] if pair[1] not in 'IJ' else positions['I/J']
    if row1 == row2: ciphertext += grid[row1][(col1 + 1) % 5] + grid[row1][(col2 + 1) % 5]
    elif col1 == col2: ciphertext += grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col1]
    else: ciphertext += grid[row2][col1] + grid[row1][col2]
  return ciphertext

def decrypt(ciphertext, key):
  grid = getMatrix(key)
  pairs = getPairs(ciphertext.upper())
  positions = getPositions(grid)
  plaintext = ""
  for pair in pairs:
    [row1, col1] = positions[pair[0]] if pair[0] not in 'IJ' else positions['I/J']
    [row2, col2] = positions[pair[1]] if pair[1] not in 'IJ' else positions['I/J']
    if row1 == row2: plaintext += grid[row1][(col1 + 1) % 5] + grid[row1][(col2 + 1) % 5]
    elif col1 == col2: plaintext += grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col1]
    else: plaintext += grid[row2][col1] + grid[row1][col2]
  return plaintext

key = input("Enter keyword: ").upper()
text = input("Enter message: ")
e = encrypt(text, key)
d = decrypt(e, key)
print(f"Encrpyted message: {e}")
print(f"Decrpyted message: {d}")