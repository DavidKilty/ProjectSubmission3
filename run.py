
print("Welcome to the Snake Pit.")
print("In this game, you will play against the computer by trying to guess where they have placed their 'snakes' on their board.")
print("The board is a 5 x 5 frame, and you can specify where you think the snakes are positioned by typing in two different numbers, both between 1 and 5.")
print("If your guess matches up with where the snakes are laying on the opposing board, you win.")
print("Keep going until you, or the computer, has won the game!")
print()

import random


BOARD_SIZE = 5
SNAKE_LENGTHS = [2, 3]  


def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]


def print_board(board):
    for row in board:
        print(' '.join(row))


def place_snake(board, snake_length):
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


def take_shot(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'  # Crush
        return True
    elif board[row][col] == '~':
        board[row][col] = 'O'  # Miss
        return False
    return None  # Invalid step


def all_snakes_crushed(board):
    return all(cell != 'S' for row in board for cell in row)


def get_player_input():
    while True:
        try:
            coords = input("Enter row and column (e.g., 2 3): ").split()
            if len(coords) != 2:
                raise ValueError("Invalid input format.")
            row, col = map(int, coords)
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                raise ValueError("Coordinates out of bounds.")
            return row, col
        except ValueError as e:
            print(e)

def computer_turn(board):
    while True:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if board[row][col] in ('~', 'S'):
            crush = take_shot(board, row, col)
            print(f"Computer shot at ({row}, {col}):{'Crush' if crush else 'Miss'}")
            break


def play_game():
    player_board = setup_board()
    computer_board = setup_board()

    while True:
        print("\nPlayer's Board:")
        print_board(player_board)
        print("\nComputer's Board:")
        print_board([['~' if cell == 'S' else cell
                    for cell in row] for row in computer_board])

        # Player turn
        print("\nYour turn!")
        row, col = get_player_input()
        crush = take_shot(computer_board, row, col)
        print(f"\nShot at ({row}, {col}): {'Crush' if crush else 'Miss'}")

        if all_snakes_crushed(computer_board):
            print("Congratulations! You crushed all the snakes!")
            break

        # Computer turn
        print("\nComputer's turn!")
        computer_turn(player_board)

        if all_snakes_crushed(player_board):
            print("You lost! The computer crushed all your snakes!")
            break


# Run game

play_game()