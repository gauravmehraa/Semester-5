def display(map):
  for row in map:
    for col in row:
      print(col, end='')
    print()

def dfs(map, x, y, moves, directions):
  if directions: return
  if x < 0 or y < 0: return
  if x >= len(map) or y >= len(map[0]): return
  if map[x][y] == 'G': 
    directions.append(moves)
    return
  if map[x][y] != '0': return
  map[x][y] = 'X'
  dfs(map, x + 1, y, moves+["D"], directions)
  dfs(map, x - 1, y, moves+["U"], directions)
  dfs(map, x, y + 1, moves+["R"], directions)
  dfs(map, x, y - 1, moves+["L"], directions)
  map[x][y] = '0'

def findGold(start):
  x, y = start
  if map[x][y] != '0':
    print("Cell not empty")
    return
  directions = []
  dfs(map, x, y, [], directions)
  if not directions: print("No path found")
  else:
    print(f"Moves: {len(directions[0])}")
    print(directions[0])

map = [['0', '0', '0', '0', '0'],
       ['0', '1', '1', '1', '1'],
       ['0', '0', '0', '0', '0'],
       ['1', '0', '0', '0', '0'],
       ['0', '0', '0', '1', '0'],
       ['0', '1', '0', '0', '0'],
       ['0', '1', '1', '1', '0'],
       ['0', '0', 'G', '0', '0']]

map = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
    ['0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
    ['0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'G']
]


display(map)

findGold((0, 0))