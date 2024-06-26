
def matrix(keyword):
  keywordset = set(keyword)
  grid = [['_' for _ in range(5)] for _ in range(5)]
  letter = 65
  for row in range(5):
    for col in range(5):
      if letter == 73:
        grid[row][col] = 'I/J'
        letter += 1
      else: grid[row][col] = chr(letter)
      letter += 1
  return grid

playfair = matrix("NETWORK")
for i in range(5):
  for j in range(5):
    print(playfair[i][j], end = '\t')
  print()