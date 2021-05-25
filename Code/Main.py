import numpy as np
import pygame
import sys
import math
from tkinter import *
G = (0, 255, 0)
B = (0, 0, 0)
W = (255, 255, 255)
R = (255, 0, 0)
Y = (255, 255, 0)
RADIUS = 45
ROW_COUNT = 6
COLUMN_COUNT = 7
SIZE = 100


class Screen:
    def __init__(self, title, w=COLUMN_COUNT * SIZE, h=(COLUMN_COUNT+1) * SIZE):
        self.title = title
        self.w = w
        self.h = h
        self.current = False

    def make_current(self):
        pygame.display.set_caption(self.title)
        self.current=True
        self.screen = pygame.display.set_mode((self.w, self.h))

    def not_current(self):
        self.current = False

    def get_screen(self):
        return self.screen

    def update(self):
        if self.current:
            self.screen.fill(B)


class Button:
    def __init__(self, xx, yy, w, h, font, window, i=0):
        self.x = xx
        self.y = yy
        self.w = w
        self.h = h
        self.font = font
        self.i = i
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, W, (self.x, self.y, self.w, self.h))
        self.window.blit(myfont.render(str(i+1),False, B),(self.x+10, self.y-10))

    def draw_res(self):
        pygame.draw.rect(self.window, W, (self.x, self.y, self.w, self.h))
        self.window.blit(myfont.render("RESET",False, B),(self.x+10, self.y-10))

    def get_pos(self):
        return self.x, self.y


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


def button_pressed(w, h, but):
    pos_m = pygame.mouse.get_pos()
    pos = but.get_pos()
    if pos[0] < pos_m[0] < pos[0]+w and pos[1] < pos_m[1] < pos[1]+h:
        return True
    else:
        return False


def reset(tur):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            board[i][j] = 0
    tur = 0
    pygame.draw.rect(screen, B, (400, 700, 500, 500))
    text1 = myfont.render('Tura gracza 1', True, Y)
    screen.blit(text1, (400, 700))
    draw_board(board)
    return tur


def won(who):
    if who == 0:
        screen.blit(myfont.render("Player 1 wins! Congratulation", False, W), (100, 400))
        screen.blit(otherfont.render("Press anywhere to reset!", False, W), (200, 500))
    else:
        screen.blit(myfont.render("Player 2 wins! Congratulation", False, W), (100, 400))
        screen.blit(otherfont.render("Press anywhere to reset!", False, W), (200, 500))


board = create_board()
print(board)
game_over = False
turn = 0
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)
otherfont = pygame.font.SysFont('Comic Sans MS', 25)
screen_basic = Screen("Connect four")
screen_winning = Screen("WINNER!!!")
screen_winning.make_current()
screen_win = screen_winning.get_screen()
screen_basic.make_current()
screen = screen_basic.get_screen()
draw_board(board)
column_buttons = []
reset_button = Button(100, 725, 150, 50, myfont, screen_win)
reset_button.draw_res()
x = 25
y = 25
for i in range(0, COLUMN_COUNT):
    column_buttons.append(Button(x, y, 50, 50, myfont, screen, i))
    column_buttons[i].draw()
    x += 100
    pygame.display.update()
    text = myfont.render('Tura gracza 1', True, Y)
    screen.blit(text, (400, 700))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if button_pressed(150, 50, reset_button):
                turn = reset(turn)
            for i in range(0, COLUMN_COUNT):
                if button_pressed(50, 50, column_buttons[i]):
                    if turn == 0:
                        pygame.draw.rect(screen, B, (400, 700, 500, 500))
                        text = myfont.render('Tura gracza 2', True, Y)
                        screen.blit(text, (400, 700))
                        col = int(math.floor(event.pos[0]/SIZE))
                        if correct_location(board, col):
                            row = next_free_space(board, col)
                            drop(board, col, row, 1)
                            if winning_check(board, 1):
                                screen_winning.make_current()
                                screen_basic.not_current()
                                screen_winning.update()
                                won(0)
                                pygame.display.update()
                                print("Player 1 Wins")
                                game_over = True
                    else:
                        pygame.draw.rect(screen, B, (400, 700, 500, 500))
                        text = myfont.render('Tura gracza 1', True, Y)
                        screen.blit(text, (400, 700))
                        col = int(math.floor(event.pos[0]/SIZE))
                        if correct_location(board, col):
                            row = next_free_space(board, col)
                            drop(board, col, row, 2)
                            if winning_check(board, 2):
                                screen_winning.make_current()
                                screen_basic.not_current()
                                screen_winning.update()
                                won(1)
                                pygame.display.update()
                                print("Player 2 Wins")
                                game_over = True
                    turn += 1
                    turn = turn % 2
                    print(board)
                    if screen_basic.current:
                        draw_board(board)
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            screen_basic.make_current()
            screen_winning.not_current()
            screen_basic.update()
            turn = reset(turn)
            game_over = False
            for i in range(0, COLUMN_COUNT):
                column_buttons[i].draw()
            reset_button.draw_res()
            draw_board(board)
            pygame.display.update()
