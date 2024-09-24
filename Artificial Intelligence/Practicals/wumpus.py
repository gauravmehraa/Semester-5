import random
from collections import defaultdict

PITS = 3
SIZE = 4

class Player:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.isAlive = True
        self.hasArrow = True
        self.canMove = True
        self.killedWumpus = False

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wumpus = False
        self.pit = False
        self.gold = False
        self.stench = False
        self.breeze = False
    

class World:
    def __init__(self, size):
        self.size = size
        self.nodes = [[Node(x, y) for y in range(size)] for x in range(size)]
        self.placeGold()
        self.placeWumpus()
        self.placePits()
        self.update()
    
    # Place Gold in a Random Cell (except 0, 0)
    def placeGold(self):
        x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
        while True:
            if x == 0 and y == 0:
                x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            else:
                self.nodes[x][y].gold = True
                break
    
    # Place Wumpus in a Random Cell (except 0, 0)
    def placeWumpus(self):
        x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
        while True:
            if (x == 0 and y == 0) or self.nodes[x][y].gold:
                x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            else:
                self.nodes[x][y].wumpus = True
                break
    
    # Place some number of Pits in Random Cells (except 0, 0)
    def placePits(self):
        placed = 0
        while placed < PITS:
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            if (x == 0 and y == 0) or self.nodes[x][y].gold or self.nodes[x][y].wumpus or self.nodes[x][y].pit:
                continue
            self.nodes[x][y].pit = True
            placed += 1

    # Place Stench and Breeze Cells wherever required
    def update(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.nodes[x][y].wumpus:
                    if x != 0: self.nodes[x-1][y].stench = True
                    if x != self.size-1: self.nodes[x+1][y].stench = True
                    if y != 0: self.nodes[x][y-1].stench = True
                    if y != self.size-1: self.nodes[x][y+1].stench = True
                if self.nodes[x][y].pit:
                    if x != 0: self.nodes[x-1][y].breeze = True
                    if x != self.size-1: self.nodes[x+1][y].breeze = True
                    if y != 0: self.nodes[x][y-1].breeze = True
                    if y != self.size-1: self.nodes[x][y+1].breeze = True
    
    def display(self, player):
        for x in range(self.size):
            print('-'*SIZE*5)
            for y in range(self.size):
                print(' | ', end='')
                if player.position is self.nodes[x][y]: print("A", end=' ')
                elif self.nodes[x][y].gold: print("G", end=' ')
                elif self.nodes[x][y].wumpus: print("W", end=' ')
                elif self.nodes[x][y].pit: print("P", end=' ')
                else: print(".", end=' ')
            print()
        print('-'*SIZE*5)
        print()

class KnowledgeBase:
    def __init__(self):
        self.knowledge = defaultdict(set)
    
    def update(self, position, info):
        self.knowledge[position].add(info)

    def remove(self, position, info):
        if info in self.knowledge[position]:
            self.knowledge[position].remove(info)
    
    def show(self):
        for node in self.knowledge:
            if len(self.knowledge[node]):
                print(node, self.knowledge[node])

class AI:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.world = World(SIZE)
        self.player = Player(self.world.nodes[0][0], "Right")
        self.visited = {(0, 0)}
        self.steps = 0
        self.stack = []

    def getAction(self, stench, breeze, gold):
        position = self.player.position
        if gold: return "Grab"
        if breeze: self.onBreeze(position)
        if stench: self.onStench(position)
        
        possible = []
        for direction in ["Up", "Down", "Left", "Right"]:
            nextNode = self.getNewPosition(direction)
            if nextNode and self.isSafe(nextNode) and (nextNode.x, nextNode.y) not in self.visited:
                possible.append(direction)

        if possible:
            direction = random.choice(possible)
            self.stack.append((self.player.position, self.player.direction))
            return direction
        else: return None

    def getNewPosition(self, direction):
        position = self.player.position
        x, y = position.x, position.y
        if direction == "Right" and y != self.world.size-1: return self.world.nodes[x][y + 1]
        if direction == "Left" and y != 0: return self.world.nodes[x][y - 1]
        if direction == "Up" and x != 0: return self.world.nodes[x - 1][y]
        if direction == "Down" and x != self.world.size-1: return self.world.nodes[x + 1][y]
        return None

    def isSafe(self, position):
        return "P" not in self.kb.knowledge[(position.x, position.y)] and "W" not in self.kb.knowledge[(position.x, position.y)] and "~P" not in self.kb.knowledge[(position.x, position.y)] and "~W" not in self.kb.knowledge[(position.x, position.y)]
    
    def onEmpty(self, position):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            x, y = position.x + dx, position.y + dy
            if 0 <= x < self.world.size and 0 <= y < self.world.size:
                self.kb.remove((x, y), "~P") 
                self.kb.remove((x, y), "~W") 

    def onBreeze(self, position):
        self.kb.update((position.x, position.y), "B")
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            x, y = position.x + dx, position.y + dy
            if 0 <= x < self.world.size and 0 <= y < self.world.size:
                if (x, y) not in self.visited: self.kb.update((x, y), "~P") 

    def onStench(self, position):
        if not self.player.killedWumpus:
            self.kb.update((position.x, position.y), "S")
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                x, y = position.x + dx, position.y + dy
                if 0 <= x < self.world.size and 0 <= y < self.world.size:
                    if (x, y) not in self.visited: self.kb.update((x, y), "~W")

    def move(self, direction):
        position = self.player.position
        x, y = position.x, position.y
        if direction == "Right": self.player.position = self.world.nodes[x][y+1]
        elif direction == "Left": self.player.position = self.world.nodes[x][y-1]
        elif direction == "Up": self.player.position = self.world.nodes[x-1][y]
        elif direction == "Down": self.player.position = self.world.nodes[x+1][y]
        self.visited.add((self.player.position.x, self.player.position.y))
        self.onEmpty(self.player.position)
    
    def killWumpus(self, position):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            x, y = position.x + dx, position.y + dy
            if 0 <= x < self.world.size and 0 <= y < self.world.size:
                if self.world.nodes[x][y].wumpus:
                    print("Shooting Wumpus")
                    self.world.nodes[x][y].wumpus = False
                    self.kb.remove((x, y), "S") 
                    self.kb.remove((position.x, position.y), "S")
                    self.kb.remove((position.x, position.y), "~W")
                    self.kb.remove((x, y), "~W") 
                    self.onEmpty(position)
                    self.player.hasArrow = False
                    self.player.killedWumpus = True
        

    def start(self):
        while self.player.isAlive:
            print('\n')
            print('*' * 100)
            self.steps += 1
            print(f"Step {self.steps}: ")
            self.world.display(self.player)
            stench = self.world.nodes[self.player.position.x][self.player.position.y].stench
            breeze = self.world.nodes[self.player.position.x][self.player.position.y].breeze
            gold = self.world.nodes[self.player.position.x][self.player.position.y].gold
            action = self.getAction(stench, breeze, gold)

            if action == "Grab":
                print("Player grabs Gold")
                break
            elif action:
                self.move(action)
                if self.world.nodes[self.player.position.x][self.player.position.y].wumpus:
                    self.player.isAlive = False
                    print("Player killed by Wumpus")
                elif self.world.nodes[self.player.position.x][self.player.position.y].pit:
                    self.player.isAlive = False
                    print("Player falls into Pit")
            else:
                self.killWumpus(self.player.position)
                if not self.stack: 
                    print("No Possible Moves")
                    break
                previousNode, previousDirection = self.stack.pop()
                self.player.position = previousNode # Backtracking
                print(f"Backtracked to {(self.player.position.x, self.player.position.y)}")
        self.kb.show()

if __name__ == "__main__":
    agent = AI()
    agent.start()