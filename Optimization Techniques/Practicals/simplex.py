def display(equations, delta):
  print(end='\t\t')
  for i in range(m + n):
    print(equations[0][i], end = '\t')
  print()
  print('Cb', end = '\t')
  print('Xb', end = '\t')
  for i in range(m): print(f'x{i+1}', end = '\t')
  for i in range(n): print(f'S{i+1}', end = '\t')
  print()

  for i in range(len(equations)):
    if i == 0: continue # for z
    for coeff in equations[i]:
      print(coeff, end = '\t')
    print()

  print(end='\t\t')
  print()
  print(delta)
  for i in range(m + n):
    print(delta[i], end='\t')

def getCoefficients(equation, eqno):
  coefficients = []
  if eqno != '': coefficients.append(0.0)
  i = 0
  while i < len(equation):
    if equation[i] == '+': pass
    elif equation[i] == '<=': pass
    elif 'x' in equation[i]:
      digit = equation[i][:equation[i].index('x')]
      if (i > 0 and equation[i-1] == '-') or equation[i][0] == '-': factor = -1.0
      else: factor = 1.0
      coeff = factor if digit == '' or digit == '-' else factor * float(digit)
      i += 1
      coefficients.append(coeff)
    else:
      coeff = float(equation[i])
      coefficients.insert(1, coeff)
      i += 1
    i += 1
  
  if eqno != '': # dont insert for z
    for i in range(n):
      identity = 0.0
      if i == eqno: identity = 1.0
      coefficients.append(identity)
  else:
    for _ in range(n): coefficients.append(0.0)
  return coefficients

def solve(equations):
  delta = []
  for row in range(1, m):
    deltaj = 0
    for column in range(2, m + n + 1):
      deltaj += (equations[row][0] * equations[row][column])
    delta.append(deltaj - equations[0][column-2])
  return delta

equations = []
m = int(input("Enter no. of variables: "))
n = int(input("Enter no. of constraints: "))
z = input("Enter z: ")
equations.append(getCoefficients(z.split(), ''))
for i in range(n):
  eq = input(f"Enter constraint {i+1}: ")
  equations.append(getCoefficients(eq.split(), i))
delta = solve(equations)
display(equations, delta)