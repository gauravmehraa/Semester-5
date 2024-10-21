def minimax(nodes, depth, alpha, beta, player1, index=0):
    if depth == 0 or 2*index >= len(nodes): return nodes[index]

    if player1:
        maximum = float('-inf')
        maximum = max(maximum, minimax(nodes, depth-1, alpha, beta, False, 2*index))
        alpha = max(alpha, maximum)
        if beta <= alpha: return maximum
        maximum = max(maximum, minimax(nodes, depth-1, alpha, beta, False, 2*index+1))
        alpha = max(alpha, maximum)
        return maximum

    else:
        minimum = float('inf')
        minimum = min(minimum, minimax(nodes, depth-1, alpha, beta, True, 2*index))
        beta = min(beta, minimum)
        if beta <= alpha: return minimum
        minimum = min(minimum, minimax(nodes, depth-1, alpha, beta, True, 2*index+1))
        beta = min(beta, minimum)
        return minimum

def main():
    depth = int(input("Enter depth of tree: "))
    nodes = [0 for _ in range(2 ** depth)]
    # nodes = [2, 3, 5, 9, 0, 1, 7, 5] depth = 3, best = 3 for p1, 5 for p2
    for i in range(len(nodes)):
        nodes[i] = int(input(f"Enter value of terminal node {i+1}: "))
    best = minimax(nodes, depth, float('-inf'), float('inf'), True)
    print(f"\nBest for Player 1: {best}")

main()