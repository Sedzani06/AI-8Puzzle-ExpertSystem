from heapq import heappush, heappop #  used to create a priority queue

# Define the goal state we want to reach
# zero represents the blank tile
GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# Directions of the movement of blank tile(0): can move Up, Down, Left, Right
DIRECTIONS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# Class for storing information about each puzzle state
class Node:
    def __init__(self, board, parent, g, move):
        self.board = board                  # Puzzle configuration
        self.parent = parent                # Previous state
        self.g = g                          # Cost so far
        self.h = self.heuristic()           # Estimated cost to goal
        self.move = move                    # Move taken to reach this node

    def f(self):
        return self.g + self.h              # Total cost( f(n)= g(n)+ h(n))

    # this function calculates how far each tile is from where it should be
    # we add up all the distance to estimate how close we are to solving the puzzle
    def heuristic(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    target_x = (value - 1) // 3
                    target_y = (value - 1) % 3
                    cost += abs(i - target_x) + abs(j - target_y)
        return cost

    def __lt__(self, other):
        return self.f() < other.f()  # For priority queue ordering

# Get blank tile position
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

# Generate possible next states
def get_neighbors(node):
    neighbors = []
    x, y = find_blank(node.board)

    for move, (dx, dy) in DIRECTIONS.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in node.board]
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            neighbors.append(Node(new_board, node, node.g + 1, move))
    return neighbors

# Reconstruct path from goal to start
def reconstruct_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path[::-1]  # Reverse path

# A* Search Algorithm to solve the 8 puzzle 
def a_star(start):
    open_set = []  # priority queue to pick the best state to try next
    visited = set()  #  stores already visited states

    # create the first puzzle state and add it to the queue
    start_node = Node(start, None, 0, "")
    heappush(open_set, (start_node.f(), start_node))

    while open_set:
         # pick the state with the lowest total cost
        _, current = heappop(open_set)

        if current.board == GOAL:
            return reconstruct_path(current)

        visited.add(str(current.board))

        for neighbor in get_neighbors(current):
            # if we have not seen this state before, add it to the queue
            if str(neighbor.board) not in visited:
                heappush(open_set, (neighbor.f(), neighbor))

    return None

# Print the board
def print_board(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else ' ' for num in row))
    print("--------")

# This is where the program starts running
if __name__ == "__main__":
    # Starting board layout (o is the blank tile)
    start_board = [[1, 2, 3],
                   [4, 0, 5],
                   [6, 7, 8]]

    solution = a_star(start_board)

    if solution:
        print("A* found a solution!")
        print("Total steps:", len(solution) - 1)
        print()
        for node in solution:
            if node.move:
                print("Move:", node.move)
            print_board(node.board)
    else:
        print("No solution found.")
