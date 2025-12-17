# Solving the 8-puzzle using Breadth-First Search (BFS)

from collections import deque

# Define the goal state of the 8-puzzle
# zero represemt a blank tile
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Directions to move the blank tile (0): up, down ,left, right,
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# This class stores each state of the puzzle
class PuzzleState:
    def __init__(self, board, x, y, depth):
        self.board = board        # The current puzzle configuration
        self.x = x                # Row of the blank tile
        self.y = y                # Column of the blank tile
        self.depth = depth        # Number of moves made so far

# Function to check if a goal state is solved
def is_goal(board):
    return board == goal_state

# Function to make sure a tile is inside the puzzle grid
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Function to print the board nicely
def print_board(board):
    for row in board:
        print(' '.join(str(num) for num in row))
    print('--------')

# Breadth-First Search to solve the puzzle
def bfs(start_board, blank_x, blank_y):
    visited = set()   # keeps track of already visited states
    queue = deque()   # queue to store puzzle states to explore

    # Add  the initial state to the queue
    initial_state = PuzzleState(start_board, blank_x, blank_y, 0)
    queue.append(initial_state)
    visited.add(tuple(tuple(row) for row in start_board))  # convert board to hashable format

    while queue:
        current = queue.popleft()
        # show current board and depth
        print(f"Depth: {current.depth}")
        print_board(current.board)

        # check if this is the goal
        if is_goal(current.board):
            print(f"Goal reached in {current.depth} moves!")
            return
        
        #Try all possible blank tile moves
        for dx, dy in moves:
            new_x = current.x + dx
            new_y = current.y + dy

            if is_valid(new_x, new_y):
                # Make a new board by swapping tiles
                new_board = [row[:] for row in current.board]
                new_board[current.x][current.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[current.x][current.y]

                # Convert to tuple for checking if visited
                board_tuple = tuple(tuple(row) for row in new_board)
                
                #if this board hasn't been visited , add it to the queue
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    queue.append(PuzzleState(new_board, new_x, new_y, current.depth + 1))

    print("No solution found using BFS.")

# Run the code
if __name__ == "__main__":
    # Starting puzzle configuration (0 is the blank space)
    start_board = [[1, 2, 3],
                   [4, 0, 5],
                   [6, 7, 8]]
    blank_x, blank_y = 1, 1  # Position of the blank (0)

    print("Initial State:")
    print_board(start_board)

    bfs(start_board, blank_x, blank_y)
