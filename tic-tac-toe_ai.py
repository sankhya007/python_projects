


import random

# Constants for representing the game state
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def evaluate(board):
    if is_winner(board, PLAYER_X):
        return 10
    elif is_winner(board, PLAYER_O):
        return -10
    else:
        return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    scores = {'X': 10, 'O': -10, 'tie': 0}

    if is_winner(board, PLAYER_X):
        return scores['X'] - depth

    if is_winner(board, PLAYER_O):
        return scores['O'] + depth

    if is_full(board):
        return scores['tie']

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_eval = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)

    return best_move

def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Tic-Tac-Toe - You are X, and the AI is O.")
    print_board(board)

    while True:
        # Player's move
        print("Player's turn (row, col): ")
        row, col = map(int, input().split())
        if board[row][col] != EMPTY:
            print("Invalid move. Cell already taken. Try again.")
            continue
        board[row][col] = PLAYER_X
        print_board(board)

        # Check if player won or it's a tie
        if is_winner(board, PLAYER_X):
            print("You win!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's turn:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_O
        print(f"AI chooses: {ai_move}")
        print_board(board)

        # Check if AI won or it's a tie
        if is_winner(board, PLAYER_O):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()




