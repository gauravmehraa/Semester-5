from collections import defaultdict

def dfs(graph, start):
  visited = {start}
  helper(start, graph, visited)
  
def helper(current, graph, visited):
  visited.add(current)
  print(current, end = ' ')
  for neighbor in graph[current]:
    if neighbor not in visited:
      helper(neighbor, graph, visited)

def add(graph, u, v):
  graph[u].append(v)
  graph[v].append(u)

def main():
  graph = defaultdict(list)
  add(graph, 0, 1)
  add(graph, 0, 2)
  add(graph, 0, 3)
  add(graph, 1, 2)
  add(graph, 2, 4)

  start = int(input("Enter start node: "))
  print("Depth First Search: ")
  dfs(graph, start)

if __name__ == '__main__': main()