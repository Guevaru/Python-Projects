import random

class TicTacToe:
    def __init__(self):
        self.board = []
        self.scores = {'X': 0, 'O': 0}

    def create_board(self):
        """Create an empty 3x3 game board."""
        for i in range(3):
            row = ['-'] * 3
            self.board.append(row)

    def show_board(self):
        """Display the game board with row and column labels."""
        print("  1 2 3")
        for i, row in enumerate(self.board):
            print(i + 1, end=' ')
            for item in row:
                print(item, end=' ')
            print()

    def get_user_input(self):
        """Get valid user input for the row and column numbers."""
        while True:
            try:
                row, col = map(int, input("Enter row & column numbers to fix a spot (e.g., 2 3): ").split())
                if 1 <= row <= 3 and 1 <= col <= 3 and self.board[row - 1][col - 1] == '-':
                    return row - 1, col - 1
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

    def fix_spot(self, row, col, player):
        """Fix a spot on the game board with the player's symbol."""
        self.board[row][col] = player

    def has_player_won(self, player):
        """Check if a player has won the game."""
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Check rows
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Check columns
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True  # Check diagonals
        return False

    def is_board_filled(self):
        """Check if the game board is completely filled."""
        for row in self.board:
            if '-' in row:
                return False
        return True

    def swap_player_turn(self, player):
        """Swap the current player's turn."""
        return 'X' if player == 'O' else 'O'

    def computer_move(self):
        """Generate a random move for the computer player."""
        available_spots = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '-']
        if available_spots:
            return random.choice(available_spots)
        else:
            return None

    def start(self):
        """Start and manage the Tic Tac Toe game."""
        while True:
            self.create_board()
            player = 'X' if self.get_random_first_player() == 1 else 'O'
            game_over = False

            while not game_over:
                self.show_board()
                print(f'\nPlayer {player} turn')

                if player == 'X':
                    row, col = self.get_user_input()
                else:
                    row, col = self.computer_move()
                    if row is None:
                        print("The game is a draw!")
                        game_over = True
                        break

                self.fix_spot(row, col, player)

                if self.has_player_won(player):
                    self.show_board()
                    print(f'Player {player} wins the game!')
                    self.scores[player] += 1
                    break

                game_over = self.is_board_filled()
                if game_over:
                    self.show_board()
                    print("The game is a draw!")

                player = self.swap_player_turn(player)

            print(f'Scores - Player X: {self.scores["X"]}, Player O: {self.scores["O"]}')

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break

    def get_random_first_player(self):
        """Randomly select the starting player."""
        return random.randint(0, 1)

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
