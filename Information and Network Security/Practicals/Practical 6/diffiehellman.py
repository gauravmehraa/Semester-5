def getAlpha(q):
  for a in range(q):
    valid = True
    values = set()

    for i in range(1, q): 
      values.add((a ** i) % q)

    for i in range(1, q):
      if i not in values:
        valid = False
        break
      
    if valid:
      alpha = a
      break
  return alpha

def generatePrivate(public, alpha, q):
  return (alpha ** public) % q

def generateKey(private, public, q):
  return (private ** public) % q

def main():
  q = int(input("Enter value of q: "))
  alpha = getAlpha(q)
  aPublic = int(input("Enter public key of A: "))
  bPublic = int(input("Enter public key of B: "))
  if aPublic >= q or bPublic >= q:
    print("Public key too large")
    exit()
  aPrivate = generatePrivate(aPublic, alpha, q)
  bPrivate = generatePrivate(bPublic, alpha, q)
  print(f"A: {(aPublic, aPrivate)}")
  print(f"B: {(bPublic, bPrivate)}")

  aKey = generateKey(aPrivate, bPublic, q)
  bKey = generateKey(bPrivate, aPublic, q)
  print(f"A Shared Key: {aKey}")
  print(f"B Shared Key: {bKey}")

main()