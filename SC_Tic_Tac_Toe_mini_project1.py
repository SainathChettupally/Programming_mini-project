# Author: Sainath Chettupally
# Date: 10-06-2024
# Overview: This script simulates a two-player Tic-Tac-Toe game on a 3x3 grid. Players alternately place
# their respective marks ('X' or 'O') on the grid. The program validates each move, updates the board, and
# checks for a winning condition or a tie after every turn. The game continues until there is a winner or the
# board is full. Players can choose to play again or exit after each game.

def print_board(board):
    """Displays the current state of the board."""
    # Print column labels
    print("-----------------")
    print("|R\\C| 0 | 1 | 2 |")
    print("-----------------")

    # Loop through the rows of the board and print them with the row number
    for idx, row in enumerate(board):
        print(f"| {idx} | {' | '.join(row)} |")
        print("-----------------")
    print()  # Extra line for spacing

def reset_board():
    """Initializes a new empty game board."""
    # Create a 3x3 matrix filled with spaces representing empty slots on the board
    return [[" " for _ in range(3)] for _ in range(3)]

def validate_entry(row, col, board):
    """Checks if the move is valid and the cell is available."""
    # Ensure the row and column are within bounds and the cell is empty
    if 0 <= row < 3 and 0 <= col < 3:
        return board[row][col] == " "
    return False

def check_win(board, player_turn):
    """Determines if the current player_turn has achieved a winning combination."""
    # Verify if any row contains the same symbol for all cells
    for row in board:
        if row == [player_turn, player_turn, player_turn]:
            return True
    # Verify if any column contains the same symbol for all cells
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player_turn:
            return True
    # Check the diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == player_turn or board[0][2] == board[1][1] == board[2][0] == player_turn:
        return True
    return False


def check_full(board):
    """Determines if the board is completely filled with no available spaces."""
    # Check if there are no empty spaces left on the board
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe_game():
    """Main function for the game logic."""
    board = reset_board()
    player_turn = "X"
    print("New Game: X goes first.")
    print()
    print_board(board)
    while True:
        # Take input from user for their move
        try:
            row, col = map(int, input(f"{player_turn}'s turn.\nWhere do you want your {player_turn} placed?\nPlease enter row number and column number separated by a comma.\n").split(","))
            print(f"You have entered row #{row}\n\t\t  and column #{col}")
        except ValueError:
            print("Invalid input. Please enter row and column as two integers separated by a comma.")
            continue
        # Validate the move and place the symbol if valid
        if validate_entry(row, col, board):
            board[row][col] = player_turn
            print("Thank you for your selection.")
            # Display the updated board if no win or draw condition
            if check_win(board, player_turn)!=True and check_full(board)!=True:
                print_board(board)
        else:
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.")
                print()
            else:
                print("That cell is already taken.\nPlease make another selection.")
                print()
            continue
        # Check for win or draw conditions
        if check_win(board, player_turn):
            #print_board(board)
            print(f"{player_turn} IS THE WINNER!!!")
            print_board(board)
            break
        elif check_full(board):
            #print_board(board)
            print()
            print("DRAW! NOBODY WINS!")
            print_board(board)
            break
        # Switch the turn to the other player
        player_turn = "O" if player_turn == "X" else "X"
    # Prompt the user for another game
    option = input("Another game? Enter Y or y for yes.\n")
    if option.lower() == "y":
        tic_tac_toe_game()
    else:
        print("Thank you for playing!")

# Start the game
tic_tac_toe_game()
