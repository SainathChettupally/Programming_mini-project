# Author: Sainath Chettupally
# Date: 10-06-2024
#overview:Connect Four Game Program
#
# This is a console-based implementation of the Connect Four game.
# Players take turns dropping their tokens ('X' and 'O') into a column on a 7-column, 6-row board.
# The objective is to form a line of four tokens either horizontally, vertically, or diagonally.
# The program handles input, checks moves, updates the board, and determines the winner.

def print_board(board):
    """Displays the Connect Four board with row and column labels."""
    print("  6 | " + " | ".join(board[5]) + " |")
    print("-----------------------------------")
    print("  5 | " + " | ".join(board[4]) + " |")
    print("-----------------------------------")
    print("  4 | " + " | ".join(board[3]) + " |")
    print("-----------------------------------")
    print("  3 | " + " | ".join(board[2]) + " |")
    print("-----------------------------------")
    print("  2 | " + " | ".join(board[1]) + " |")
    print("-----------------------------------")
    print("  1 | " + " | ".join(board[0]) + " |")
    print("-----------------------------------")
    print("|R/C| a | b | c | d | e | f | g |")
    print("-----------------------------------")
    print()


def reset_board():
    """Initializes a new empty Connect Four board."""
    # Create a 6x7 matrix with spaces representing empty slots on the board.
    return [[" " for _ in range(7)] for _ in range(6)]


def validate_entry(board, col):
    """Checks if the move is valid by ensuring the column is within bounds and has space."""
    # Ensure that the column is within the board limits and has space available.
    if col<7:
        return 0 <= col < 7 and board[5][col] == " "
    return False


def available_position(board, col):
    """Finds the lowest available row in the specified column."""
    # Iterate through each row in the column from bottom to top to find the first empty position.
    for row in range(6):
        if board[row][col] == " ":
            return row
    return None  # This shouldn't happen since we already validated the column has space.


def check_full(board):
    """returns True if the board is full (i.e., no empty spaces at the top row)."""
    # Check if all columns in the top row are occupied.
    return all(board[5][col] != " " for col in range(7))


def check_win(board, row, col, player_turn):
    """Checks whether the current move results in a win."""
    # Define possible directions to check for four in a row.
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # horizontal, vertical, and two diagonals
    for dr, dc in directions:
        count = 1
        for direction in (1, -1):  # Check in both directions
            r, c = row + dr * direction, col + dc * direction
            while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player_turn:
                count += 1
                r += dr * direction
                c += dc * direction
            if count >= 4:
                return True
    return False


def convert_input(user_input):
    """Converts user input (e.g., 'a1') to column index."""
    # Define a mapping for columns using letters.
    columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
    try:
        col = columns[user_input[0].lower()]
        return col
    except (IndexError, KeyError):
        return None


def available_positions(board):
    """returns a list of the lowest available positions in each column for display."""
    positions = []
    for col in range(7):
        for row in range(6):
            if board[row][col] == " ":
                positions.append(f"{chr(97 + col)}{row + 1}")
                break
    return positions


def connect_four_game():
    """Main game loop to handle input, update the board, and determine the winner."""
    # Initialize a new game board and set the first player as 'X'.
    board = reset_board()
    player_turn = "X"
    print("New game: X goes first.")
    print_board(board)
    while True:
        # Display available positions to the player.
        available_pos = available_positions(board)
        print(f"{player_turn}'s player_turn.")
        print(f"Where do you want your {player_turn} placed?")
        print(f"Available positions are: {available_pos}")
        # Take input from user for the next move.
        user_input = input("\nPlease enter column-letter and row-number (e.g., a1): ").strip()
        col = convert_input(user_input)
        # Validate the move and place the token if valid.
        if col is not None and validate_entry(board, col):
            row = available_position(board, col)
            board[row][col] = player_turn
            print("Thank you for your selection.")
            if check_win(board, row, col, player_turn)!=True and check_full(board)!=True:
                print_board(board)
        else:
            # Inform the user if the input is invalid.
            print("Invalid move. Please try again.")
            print()
            continue
        # Check for a win or draw after the move.
        if check_win(board, row, col, player_turn):
            print()
            print(f"{player_turn} IS THE WINNER!!!")
            print_board(board)
            break
        elif check_full(board):
            print()
            print("DRAW! NOBODY WINS!")
            print_board(board)
            break
        # Switch the player_turn to the other player.
        player_turn = "O" if player_turn == "X" else "X"  # Switch player_turn between X and O

    # Prompt the user for another game.
    another_game = input("Another game (y/n)? ").lower()
    if another_game == "y":
        connect_four_game()
    else:
        print("Thank you for playing!")


# Start the game
connect_four_game()
