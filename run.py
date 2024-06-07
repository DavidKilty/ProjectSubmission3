import random

# Constants
BOARD_SIZE = 5
SNAKE_LENGTHS = [2, 3]  # Example of snake lengths

def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

def print_board(board):
    for row in board:
        print(' '.join(row))

def snake(board, snake_lenght):
    placed = False
    while not placed:
        orientation = random.choice(['H', 'V'])
        if orientation == 'H':
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - snake_length)
            if all(board[row][col + i] == '~' for i in range(snake_length)):
                for i in range(snake_length):
                    board[row][col + i] = 'S'
                placed = True
        else:
            row = random.randint(0, BOARD_SIZE - snake_length)
            col = random.randint(0, BOARD_SIZE - 1)
            if all(board[row + i][col] == '~' for i in range(snake_length)):
                for i in range(snake_length):
                    board[row + i][col] = 'S'
                placed = True

def setup_board():
    board = create_board(BOARD_SIZE)
    for snake_length in SNAKE_LENGTHS:
    place_snake(board, snake_length)
    return board

# Example usage
player_board = setup_board()
computer_board = setup_board()

print("Player's Board:")
print_board(player_board)
print("\nComputer's Board:")
print_board(computer_board)

def take_shot(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'  # Hit
        return True
    elif board[row][col] == '~':
        board[row][col] = 'O'  # Miss
        return False
    return None  # Invalid shot
def all_snakes_crushed(board):
    return all(cell != 'S' for row in board for cell in row)

