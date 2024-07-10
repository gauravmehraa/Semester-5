from collections import defaultdict
import heapq

def a_star(graph, start, end, heuristic):
  return None

def add(graph, u, v, cost):
  graph[u].append((v, cost))
  graph[v].append((u, cost))

def main():
  vertices = 5
  graph = defaultdict(list)
  add(graph, 0, 1, 1)
  add(graph, 0, 2, 4)
  add(graph, 0, 3, 7)
  add(graph, 1, 2, 2)
  add(graph, 2, 4, 3)

  heuristic = {
    0: 7,
    1: 6,
    2: 2,
    3: 4,
    4: 0 
  }

  start = int(input("Enter start node: "))
  end = int(input("Enter goal node: "))
  print("A* Search: ")
  path = a_star(graph, start, end, heuristic)
  if path: print(path)
  else: print("No path found")

if __name__ == '__main__': main()