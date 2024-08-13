from queue import PriorityQueue

class KnowledgeBase:
  def __init__(self):
    self.kb = []

  def tell(self, sentence) -> None:
    if sentence not in self.kb:
      self.kb.append(sentence)
      self.kb = sorted(self.kb, key=lambda x: len(x))

  def ask(self, query) -> bool:
    return False

  def compare(self, query1, query2) -> None:
    pass

  def remove(self, sentence) -> None:
    pass


class AI:
  def __init__(self):
    self.kb = KnowledgeBase()
    self.moves = []
    self.wumpus = True
    self.arrow = True
  
  def getAction(self, stench, breeze, glitter):
    pass

  def onBreeze(self, current):
    pass

  def onStench(self, current):
    pass

  def walk(self):
    pass

  def killWumpus(self, direction) -> None:
    if direction == "Right": pass
    elif direction == "Left": pass
    elif direction == "Up": pass
    elif direction == "Down": pass


def main():
  print('hello')
  pass

if __name__ == "__main__":
  main()