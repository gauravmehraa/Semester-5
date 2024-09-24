class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add(self, value):
        child = Node(value, parent=self)
        self.children.append(child)
        return child

def minimax(node, depth, alpha, beta, player1):
    if depth == 0 or not node.children:
        return node.value
    if player1:
        maximum = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maximum = max(maximum, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: break
        return maximum
    else:
        minimum = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, True)
            minimum = min(minimum, eval)
            beta = min(beta, eval)
            if beta <= alpha: break
        return minimum

root = Node(0)
child1 = root.add(0)
child2 = root.add(1)
child3 = root.add(2)
child1.add(3)
child1.add(4)
child2.add(5)
child2.add(6)
child3.add(7)
child3.add(8)

best = minimax(root, depth=3, alpha=float('-inf'), beta=float('inf'), player1=True)
print(f"Best value: {best}")
