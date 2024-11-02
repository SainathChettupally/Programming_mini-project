# Author: Sainath Chettupally
# Date: 10-06-2024
# Overview: This script simulates a two-player Tic-Tac-Toe game on a 3x3 grid. Players alternately place
# their respective marks ('X' or 'O') on the grid. The program validates each move, updates the board, and
# checks for a winning condition or a tie after every turn. The game continues until there is a winner or the
# board is full. Players can choose to play again or exit after each game.

class Board:
    def __init__(self):
        # Initializing a new empty game board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def printBoard(self):
        # Displays the current state of the board with row and column labels
        print("-----------------")
        print("|R\C| 0 | 1 | 2 |")
        print("-----------------")
        for idx, row in enumerate(self.board):
            print(f"| {idx} | {' | '.join(row)} |")
            print("-----------------")
        print()  # Extra line for spacing

    def updateBoard(self, row, col, player):
        # Updating the board with the player's move
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False


class Game:
    def __init__(self):
        # Initializing the game with an empty board and setting the first player to 'X'
        self.board = Board()
        self.turn = 'X'

    def switchPlayer(self):
        # Switching player between 'X' and 'O'
        self.turn = 'O' if self.turn == 'X' else 'X'

    def validateEntry(self, row, col):
        # Validating if the move is within bounds and the cell is available
        if 0 <= row < 3 and 0 <= col < 3 and self.board.board[row][col] == ' ':
            return True
        return False

    def checkFull(self):
        # Determining if the board is completely filled with no available spaces
        return all(cell != ' ' for row in self.board.board for cell in row)

    def checkWin(self):
        # Checking rows, columns, and diagonals for a winning combination
        b = self.board.board
        # Check each row for a win
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != ' ':
                return True
        # Check each column for a win
        for i in range(3):
            if b[0][i] == b[1][i] == b[2][i] != ' ':
                return True
        # Check diagonals for a win
        if b[0][0] == b[1][1] == b[2][2] != ' ' or b[0][2] == b[1][1] == b[2][0] != ' ':
            return True
        return False

    def checkEnd(self):
        # Checking if the game is over (either there is a winner or the board is full)
        if self.checkWin():
            print(f"{self.turn} IS THE WINNER!!!")
            return True
        elif self.checkFull():
            print("DRAW! NOBODY WINS!")
            return True
        return False

    def playGame(self):
        # Main function for the game logic
        self.board = Board()  # Reset the board for a new game
        self.turn = 'X'  # 'X' always goes first
        print("New Game: X goes first.")
        print()
        self.board.printBoard()
        while True:
            try:
                # Take input from user for their move
                row, col = map(int, input(f"{self.turn}'s turn.\nWhere do you want your {self.turn} placed?\nPlease enter row number and column number separated by a comma.\n").split(","))
                print(f"You have entered row #{row}\n\t\t  and column #{col}")
            except ValueError:
                print("Invalid input. Please enter row and column as two integers separated by a comma.")
                continue
            # Validate the move and update the board if valid
            if self.validateEntry(row, col):
                self.board.updateBoard(row, col, self.turn)
                print("Thank you for your selection.")
                # Display the updated board
                self.board.printBoard()
                # Check for win or draw conditions
                if self.checkEnd():
                    break
                # Switch the turn to the other player
                self.switchPlayer()
            else:
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.")
                    print()
                else:
                    print("That cell is already taken.\nPlease make another selection.")
                    print()
                continue
        # Prompt the user for another game
        option = input("Another game? Enter Y or y for yes.\n")
        if option.lower() == "y":
            self.playGame()
        else:
            print("Thank you for playing!")


# To play the game, create an instance of Game and call playGame()
if __name__ == "__main__":
    game = Game()
    game.playGame()
