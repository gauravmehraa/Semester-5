import random

def f(x): return -(x - 3)**2 + 10

def getneighbor(x, step): return x + random.choice([-step, step])

def hillclimbing(start):
  optima = start
  height = f(start)
  while True:
    neighbor = getneighbor(optima, 0.01)
    neighborheight = f(neighbor)
    if neighborheight >= optima:
      optima = neighbor
      height = neighborheight
    else: break
  return optima, height

def main():
  start = round(random.uniform(0, 10), 3)
  optima, height = hillclimbing(start)
  print(f"Starting Point: {start}")
  print(f"Local Optima: {optima}")
  print(f"f(x): {height}")

main()