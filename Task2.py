import math
GREEN = '\033[92m'  
RED = '\033[91m'    
YELLOW = '\033[93m' 
RESET = '\033[0m'   


def print_board(board):
    for row in board:
        print(
            " | ".join(
                [f"{GREEN}{cell}{RESET}" if cell == "X" else f"{RED}{cell}{RESET}" if cell == "O" else " " for cell in row]
            )
        )
        print(YELLOW + "-" * 9 + RESET)


def check_winner(board):
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a tie
    if all(cell != " " for row in board for cell in row):
        return "Tie"

    return None


def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":  # Human player
        return -10 + depth
    elif winner == "O":  # AI
        return 10 - depth
    elif winner == "Tie":
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print(YELLOW + "Welcome to Tic-Tac-Toe!" + RESET)
    print(YELLOW + "You are " + GREEN + "'X'" + YELLOW + ". The AI is " + RED + "'O'." + RESET)

    print_board(board)

    while True:
        
        while True:
            try:
                human_move = int(input(YELLOW + "Enter your move (1-9): " + RESET)) - 1
                row, col = divmod(human_move, 3)
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print(YELLOW + "Cell is already occupied. Choose another!" + RESET)
            except (ValueError, IndexError):
                print(YELLOW + "Invalid input! Enter a number between 1 and 9." + RESET)

        print_board(board)

        
        winner = check_winner(board)
        if winner:
            if winner == "X":
                print(GREEN + "Congratulations! You win!" + RESET)
            elif winner == "O":
                print(RED + "AI wins! Better luck next time." + RESET)
            else:
                print(YELLOW + "It's a tie!" + RESET)
            break

        
        print(YELLOW + "AI is making its move..." + RESET)
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"

        print_board(board)

        
        winner = check_winner(board)
        if winner:
            if winner == "X":
                print(GREEN + "Congratulations! You win!" + RESET)
            elif winner == "O":
                print(RED + "AI wins! Better luck next time." + RESET)
            else:
                print(YELLOW + "It's a tie!" + RESET)
            break


if __name__ == "__main__":
    play_game()
