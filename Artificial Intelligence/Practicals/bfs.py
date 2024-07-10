from collections import defaultdict

def bfs(graph, start):
  visited = {start}
  queue = [start]
  while queue:
    current = queue[0]
    queue = queue[1:]
    print(current, end = ' ')
    
    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

def add(graph, u, v):
  graph[u].append(v)
  graph[v].append(u)

def main():
  vertices = 5
  graph = defaultdict(list)
  add(graph, 0, 1)
  add(graph, 0, 2)
  add(graph, 0, 3)
  add(graph, 1, 2)
  add(graph, 2, 4)

  start = int(input("Enter start node: "))
  print("Breadth First Search: ")
  bfs(graph, start)

if __name__ == '__main__': main()