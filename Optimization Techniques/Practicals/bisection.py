import math
DEGREE = 5

def display(coeffs):
  print('f(x) = ', end='')
  for i in range(DEGREE, -1, -1):
    current = coeffs[DEGREE-i]
    if math.trunc(current) == int(current): current = int(current)
    if current > 0: sign = '+' if i != DEGREE else '' # ignore plus for first element
    if current < 0: sign = '-'
    if current != 0:
      current = '' if abs(current)== 1 and i != 0 else abs(current) 
      if i == 0: print(f'{sign} {current}') # ignore x^0 for last coefficient
      else: print(f'{sign} {current}x^{i}', end=' ')

def f(x):
  result = 0
  for i in range(DEGREE + 1):
    result = result + (coeffs[i] * (x ** (DEGREE - i)))
  return result

def getInterval(initial=1):
  last = -1 if f(initial-1) < 0 else 1
  for i in range(initial, initial+100):
    if last == -1 and f(i) > 0: return i-1, i, '-+'
    if last == 1 and f(i) < 0: return i-1, i, '+-'
    last = -1 if f(i) < 0 else 1
  print("No opposite signs")
  exit()

def bisection():
  lower, upper, signs = getInterval()
  while True:
    xi = (lower + upper)/2
    answer = f(xi)
    if round(answer, 5) == 0.0000:
      return xi
    if signs == '-+':
      if f(xi) < 0: lower = xi
      else: upper = xi
    else:
      if f(xi) > 0: lower = xi
      else: upper = xi

coeffs = []
for power in range(DEGREE, -1, -1):
  coeffs.append(float(input(f"Enter coefficient of x^{power}: ")))
display(coeffs)
root = bisection()
if root: print(f'Root: {root}')
else: print('No root')