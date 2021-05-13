import numpy as np
import pygame
import sys
import math
G = (0,255,0)
B = (0,0,0)
R = (255,0,0)
Y = (255,255,0)
RADIUS = 45
ROW_COUNT = 6
COLUMN_COUNT = 7
SIZE = 100
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

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, G, (c*SIZE, r*SIZE+SIZE, SIZE, SIZE))
            if board[r][c] == 0:
                pygame.draw.circle(screen, B, (c*SIZE+SIZE/2, r*SIZE+SIZE+SIZE/2), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, R, (c * SIZE + SIZE / 2, r * SIZE + SIZE + SIZE / 2), RADIUS)
            else:
                pygame.draw.circle(screen, Y, (c * SIZE + SIZE / 2, r * SIZE + SIZE + SIZE / 2), RADIUS)
    pygame.display.update()
board = create_board()
print(board)
game_over = False
turn = 0

pygame.init()
width = COLUMN_COUNT * SIZE
height = COLUMN_COUNT * SIZE
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                col = int(math.floor(event.pos[0]/SIZE))
                if correct_location(board, col):
                    row = next_free_space(board, col)
                    drop(board, col, row, 1)
                    if winning_check(board, 1):
                        print("Player 1 Wins")
                        game_over = True
            else:
                col = int(math.floor(event.pos[0]/SIZE))
                if correct_location(board, col):
                    row = next_free_space(board, col)
                    drop(board, col, row, 2)
                    if winning_check(board, 2):
                        print("Player 2 Wins")
                        game_over = True
            turn += 1
            turn = turn % 2
            print(board)
            draw_board(board)