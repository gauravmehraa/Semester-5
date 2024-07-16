import queue

def select(open):
  for node in open:
    print(node)
  return

def a_star(graph, start, end, heuristic):
  open = [start]
  path = []
  distance = 0
  fringe = queue.PriorityQueue()
  fringe.put((heuristic[start] + distance, [start, 0]))
  while not fringe.empty():
    current = fringe.get()[1]
    path.append(current)
    if current == end: break
    fringe = queue.PriorityQueue()
    for neighbor in graph[current[0]]:
      if neighbor[0] not in path: fringe.put
  return None

def add(graph, u, v, cost):
  if graph.get(u): graph[u].append((v, cost))
  else: graph[u] = [(v, cost)]
  if graph.get(v): graph[v].append((u, cost))
  else: graph[v] = [(u, cost)]

def main():
  graph = {}
  add(graph, "A", "Z", 75)
  add(graph, "A", "T", 118)
  add(graph, "A", "S", 140)
  add(graph, "Z", "O", 71)
  add(graph, "O", "S", 151)
  add(graph, "T", "L", 111)
  add(graph, "L", "M", 70)
  add(graph, "M", "D", 75)
  add(graph, "D", "C", 120)
  add(graph, "S", "R", 80)
  add(graph, "S", "F", 99)
  add(graph, "R", "C", 146)
  add(graph, "C", "P", 138)
  add(graph, "R", "P", 97)
  add(graph, "F", "B", 211)
  add(graph, "P", "B", 101)
  add(graph, "B", "G", 90)
  add(graph, "B", "U", 85)
  add(graph, "U", "H", 98)
  add(graph, "H", "E", 86)
  add(graph, "U", "V", 142)
  add(graph, "V", "I", 92)
  add(graph, "I", "N", 87)

  heuristic = {
    "A":  366, "B": 0, "C": 160, "D": 242, "E": 161, "F":167, "G": 77,
    "H": 151, "I": 226, "L": 244, "M": 241, "N": 234, "O": 380, "P": 100,
    "R": 193, "S": 253, "T": 329, "U": 80, "V": 199, "Z": 374
  }

  start = input("Enter start node: ")
  end = input("Enter goal node: ")
  path = a_star(graph, start, end, heuristic)
  if path: print(path)
  else: print("No path found")

if __name__ == '__main__': main()