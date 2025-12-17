# Solving the 8-puzzle using Depth-First Search (DFS)

# Directions for movement: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Goal state of the puzzle
# zero represents the blank tile
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Class to store each puzzle state
class PuzzleState:
    def __init__(self, board, x, y, depth):
        self.board = board        # Current configuration (3x3 board layout)
        self.x = x                # row index of the blank tile (0)
        self.y = y                # column index of the blank tile
        self.depth = depth        # Number of moves made so far

# Check if a board is in the goal state
def is_goal(board):
    return board == goal_state

# Check if a position is within the board(inside the puzzle)
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Display the board(puzzle) in a clear format
def print_board(board):
    for row in board:
        print(' '.join(str(num) for num in row))
    print("--------")

# DFS to solve the puzzle
def dfs(start_board, blank_x, blank_y):
    stack = []  # stack to explore deep paths first
    visited = set()  # tracks visited puzzle states

    # Addd the  initial state
    stack.append(PuzzleState(start_board, blank_x, blank_y, 0))
    visited.add(tuple(tuple(row) for row in start_board))

    while stack:
        current = stack.pop()

        # show board andd depth
        print(f"Depth: {current.depth}")
        print_board(current.board)

        # if goal is reached , stop here
        if is_goal(current.board):
            print(f"Goal reached in {current.depth} moves!")
            return

        # Try all 4 directions for blank tile 
        for dx, dy in moves:
            new_x = current.x + dx
            new_y = current.y + dy

            if is_valid(new_x, new_y):
                # Create new board configuration ( puzzle state) by swapping tiles
                new_board = [row[:] for row in current.board]
                new_board[current.x][current.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(tuple(row) for row in new_board)

                # Add to stack if it's a new state 
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(PuzzleState(new_board, new_x, new_y, current.depth + 1))
             
    print("No solution found using DFS.")

# Run the program
if __name__ == "__main__":
    # Starting configuration (0 = blank)
    start_board = [[1, 2, 3],
                   [4, 0, 5],
                   [6, 7, 8]]
    blank_x, blank_y = 1, 1  # Position of the blank (0) tile

    print("Initial State:")
    print_board(start_board)

    dfs(start_board, blank_x, blank_y)
