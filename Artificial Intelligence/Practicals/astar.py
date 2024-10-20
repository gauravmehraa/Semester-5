from queue import PriorityQueue
from collections import defaultdict

def a_star(graph, start, heuristic):
  fringe = PriorityQueue()
  predecessor = {}
  g_costs = { start: 0 }
  visited = set()

  fringe.put((heuristic[start], start, 0))
  while not fringe.empty():
    _, currentnode, current_g = fringe.get()
    if currentnode in visited: continue
    visited.add(currentnode)
    if currentnode == "B": return get_path(predecessor, currentnode)
    
    for neighbor, gn in graph[currentnode]:
      g_estimate = current_g + gn
      if neighbor in visited and g_estimate >= g_costs.get(neighbor, float('inf')): continue
      if g_estimate < g_costs.get(neighbor, float('inf')):
        g_costs[neighbor] = g_estimate
        fn = heuristic[neighbor] + g_costs[neighbor]
        fringe.put((fn, neighbor, g_costs[neighbor]))
        predecessor[neighbor] = currentnode
  return None

def get_path(predecessor, currentnode):
  path = [currentnode]
  while currentnode in predecessor:
    currentnode = predecessor[currentnode]
    path.insert(0, currentnode)
  return path

def add(graph, u, v, cost):
  graph[u].append((v, cost))
  graph[v].append((u, cost))

def main():
  graph = defaultdict(list)
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
    "A":  366, "B": 0, "C": 160, "D": 242, "E": 161, "F": 178, "G": 77,
    "H": 151, "I": 226, "L": 244, "M": 241, "N": 234, "O": 380, "P": 98,
    "R": 193, "S": 253, "T": 329, "U": 80, "V": 199, "Z": 374
  }

  start = input("Enter start node: ")
  path = a_star(graph, start, heuristic)
  if path: print(path)
  else: print("No path found")

if __name__ == '__main__': main()