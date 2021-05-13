import numpy as np
ROW_COUNT = 6
COLUMN_COUNT = 7
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop(board, col, row, sign):
    board[row][col] = sign


def correct_location(board, col):
    return board[0][col] == 0

def next_free_space(board, col):
    i = ROW_COUNT
    while i >= 0:
        i -= 1
        if board[i][col] == 0:
            return i

def winning_check(board, sign):
    #horizontal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == sign and board[r][c+1] == sign and board[r][c+2] == sign and board[r][c+3] == sign:
                return True
    #vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == sign and board[r+1][c] == sign and board[r+2][c] == sign and board[r+3][c] == sign:
                return True
    #diaganols+
    for c in range(0,COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == sign and board[r-1][c+1] == sign and board[r-2][c+2] == sign and board[r-3][c+3] == sign:
                return True
    #diaganols-
    for c in range(0, COLUMN_COUNT-3):
        for r in range(0,ROW_COUNT-3):
            if board[r][c] == sign and board[r+1][c+1] == sign and board[r+2][c+2] == sign and board[r+3][c+3] == sign:
                return True

board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input("Player 1 moves: "))
        if correct_location(board, col):
            row = next_free_space(board, col)
            drop(board, col, row, 1)
            if winning_check(board, 1):
                print("Player 1 Wins")
                game_over = True

    else:
        col = int(input("Player 2 moves: "))
        if correct_location(board, col):
            row = next_free_space(board, col)
            drop(board, col, row, 2)
            if winning_check(board, 2):
                print("Player 2 Wins")
                game_over = True
    turn +=1
    turn = turn%2
    #print(select)
    #print(type(select))
    print(board)