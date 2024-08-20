class Player:
  def __init__(self, state, direction):
    self.state = state
    self.direction = direction
    self.hasGold = False
    self.killedWumpus = False
    self.isLeaving = False

  def move(self, states):
    pass

  def turnLeft(self):
    pass

  def turnRight(self):
    pass

  def __repr__(self) -> str:
    return (f"Current State: {self.state.name}\nCurrent Direction: {self.direction}")

class Node:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.name = f"{str(self.row)}, {str(self.col)}"
    
    self.right = ""
    self.left = ""
    self.up = ""
    self.down = ""

  def __repr__(self):
    return (f"Name: {str(self.name)}\nL: {self.left}\nR: {self.right}\nU: {self.up}\nD: {self.down}")

class States:
  def __init__(self):
    self.states = dict()
    self.visited = []
    self.unvisitedSafe = []
    self.maxRow = -1
    self.maxCol = -1
  
  def add(self, node):
    if self.maxCol != -1 and node.column == self.maxCol: node.right = "W"
    else: node.right = str(node.row) + ", " + str(node.column+1)

    if node.column-1 == 0: node.left = "W"
    else: node.left = str(node.row) + ", " + str(node.column-1)

    if self.maxRow != -1 and node.row == self.maxRow: node.up = "W"
    else: node.up = str(node.row+1) + ", " + str(node.column)

    if node.row-1 == 0: node.down = "W"
    else: node.down = str(node.row-1) + ", " + str(node.column)

    self.states[node.name] = node
    if node.name not in self.visited: self.visited.append(node.name)

  def __repr__(self):
    return (f"States: {str(self.states.keys())}\nVisited: {str(self.visited)}")

class KnowledgeBase:
  def __init__(self):
    self.kb = []

  def tell(self, sentence) -> None:
    if sentence not in self.kb:
      self.kb.append(sentence)
      self.kb = sorted(self.kb, key=lambda x: len(x)) # sort knowledge base by length

  def ask(self, query) -> bool:
    KB = ['hello1', 'hello2']
    KB_temp=[[item2 for item2 in item] for item in KB]
    print(KB_temp)
    return False

  def compare(self, query1, query2) -> None:
    pass

  def remove(self, sentence) -> None:
    pass


class AI:
  def __init__(self):
    self.kb = KnowledgeBase()
    self.player = Player("1, 1", "Right")
    self.moves = []
    self.states = States()


    self.kb.add(["~P1, 1"])
    self.kb.add(["~W1, 1"])
    self.states.add(Node(1, 1))

    self.wumpusAlive = True
    self.hasArrow = True
    self.wumpusDirections = ["Right", "Left", "Up", "Down"]
  
  def getAction(self, stench, breeze, glitter):
    pass

  def onBreeze(self, current):
    pass

  def onStench(self, current):
    pass

  def onBump(self):
    pass

  def walk(self):
    pass

  def checkWumpus(self, current):
    pass

  def killWumpus(self, direction) -> None:
    if direction == "Right": pass
    elif direction == "Left": pass
    elif direction == "Up": pass
    elif direction == "Down": pass

  def checkSafe(self, current):
    pass


def main():
  print('hello')
  kb = KnowledgeBase()
  kb.ask('1')
  pass

if __name__ == "__main__":
  main()