# Initialize the board as an empty 3x3 grid
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if the game is over
def check_game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    # Check for a draw
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True

    return False

# Function to play the game
def play_game():
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Player {current_player}, enter row and column (e.g., 1 2): ")
        row, col = map(int, input().split())

        if board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_game_over(board):
            display_board(board)
            if check_game_over(board) and not any(' ' in row for row in board):
                print("It's a draw!")
            else:
                print(f"Player {current_player} wins!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
