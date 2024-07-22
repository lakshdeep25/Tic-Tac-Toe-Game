import random

def print_board(board):
    for row in board:
        print(' '.join(row))

def check_win(board, sign):
    # Check rows, columns and diagonals
    for row in board:
        if all(s == sign for s in row):
            return True
    for col in range(3):
        if all(row[col] == sign for row in board):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def get_free_positions(board):
    free_positions = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == '.':
                free_positions.append((r, c))
    return free_positions

def make_move(board, position, sign):
    row, col = position
    board[row][col] = sign

def get_user_move(board):
    valid_move = False
    while not valid_move:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                row, col = divmod(move-1, 3)
                if board[row][col] == '.':
                    valid_move = True
                    return (row, col)
        print("Invalid move. Try again.")

def main():
    board = [['.' for _ in range(3)] for _ in range(3)]
    board[1][1] = 'X'  # Computer's first move in the middle
    print_board(board)

    while True:
        # User's move
        user_move = get_user_move(board)
        make_move(board, user_move, 'O')
        print_board(board)

        if check_win(board, 'O'):
            print("You win!")
            break
        if not get_free_positions(board):
            print("It's a tie!")
            break

        # Computer's move
        free_positions = get_free_positions(board)
        computer_move = random.choice(free_positions)
        make_move(board, computer_move, 'X')
        print_board(board)

        if check_win(board, 'X'):
            print("Computer wins!")
            break
        if not get_free_positions(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()






