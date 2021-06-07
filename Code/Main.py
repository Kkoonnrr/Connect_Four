import pygame
import math
from tkinter import *
from Code.WrongMoveError import WrongMoveError
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
RADIUS = 45
ROW_COUNT = 6
COLUMN_COUNT = 7
SIZE = 100


class Mode:
    def __init__(self, screen, myfont, otherfont, board=None):
        if board is None:
            self.board = [[]]
        self.otherfont = otherfont
        self.myfont = myfont
        self.screen = screen
        self.board = board

    def winning_check(self, sign):
        raise NotImplementedError('No mode')

    def create_board(self):
        self.board = [[0 for i in range(7)] for i in range(6)]
        return self.board

    def drop(self, col, row, sign):
        self.board[row][col] = sign

    def correct_location(self, col):
        return self.board[0][col] == 0

    def next_free_space(self, col):
        i = ROW_COUNT
        while i >= 0:
            i -= 1
            if self.board[i][col] == 0:
                return i
        else:
            raise WrongMoveError

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLACK, (c * SIZE, r * SIZE + SIZE, SIZE, SIZE))
                if self.board[r][c] == 0:
                    pygame.draw.circle(self.screen, WHITE, (c * SIZE + SIZE / 2, r * SIZE + SIZE + SIZE / 2), RADIUS)
                elif self.board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (c * SIZE + SIZE / 2, r * SIZE + SIZE + SIZE / 2), RADIUS)
                else:
                    pygame.draw.circle(self.screen, YELLOW, (c * SIZE + SIZE / 2, r * SIZE + SIZE + SIZE / 2), RADIUS)
        pygame.display.update()

    def button_pressed(self, w, h, but):
        pos_m = pygame.mouse.get_pos()
        pos = but.get_pos()
        if pos[0] < pos_m[0] < pos[0] + w and pos[1] < pos_m[1] < pos[1] + h:
            return True
        else:
            return False

    def selected_mode(self, w, h, new_mode, old_mode, text, text2):
        pos_m = pygame.mouse.get_pos()
        pos = new_mode.get_pos()
        pos2 = old_mode.get_pos()
        if pos[0] < pos_m[0] < pos[0] + w and pos[1] < pos_m[1] < pos[1] + h:
            pygame.draw.rect(self.screen, BLUE, (pos[0] - 2, pos[1] - 2, w + 4, h + 4))
            new_mode.draw_text(text)
            pygame.draw.rect(self.screen, BLACK, (pos2[0] - 2, pos2[1] - 2, w + 4, h + 4))
            old_mode.draw_text(text2)
            self.reset()
            self.draw_board()
            return True
        else:
            return False

    def reset(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                self.board[i][j] = 0
        tur = 0
        pygame.draw.rect(self.screen, BLACK, (400, 700, 500, 500))
        text1 = self.myfont.render('Player 1 turn', True, YELLOW)
        self.screen.blit(text1, (400, 700))
        self.draw_board()
        return tur

    def won(self, who):
        if who == 0:
            self.screen.blit(self.myfont.render("Player 1 wins! Congratulation", False, WHITE), (100, 400))
            self.screen.blit(self.otherfont.render("Press anywhere to reset!", False, WHITE), (200, 500))
        else:
            self.screen.blit(self.myfont.render("Player 2 wins! Congratulation", False, WHITE), (100, 400))
            self.screen.blit(self.otherfont.render("Press anywhere to reset!", False, WHITE), (200, 500))

    def get_board(self):
        return self.board

    def full_board(self):
        return not any(0 in ROW_COUNT for ROW_COUNT in self.board)
class FourInRow(Mode):
    def winning_check(self, sign):
        # horizontal
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == sign and self.board[r][c + 1] == sign and self.board[r][c + 2] == sign\
                        and self.board[r][c + 3] == sign:
                    return True
        # vertical
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == sign and self.board[r + 1][c] == sign and self.board[r + 2][c] == sign\
                        and self.board[r + 3][c] == sign:
                    return True
        # diagonal+
        for c in range(0, COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == sign and self.board[r - 1][c + 1] == sign and self.board[r - 2][c + 2] == sign\
                        and self.board[r - 3][c + 3] == sign:
                    return True
        # diagonal-
        for c in range(0, COLUMN_COUNT - 3):
            for r in range(0, ROW_COUNT - 3):
                if self.board[r][c] == sign and self.board[r + 1][c + 1] == sign and self.board[r + 2][c + 2] == sign\
                        and self.board[r + 3][c + 3] == sign:
                    return True


class FiveInRow(Mode):
    def winning_check(self, sign):
        # horizontal
        for c in range(COLUMN_COUNT - 4):
            for r in range(ROW_COUNT):
                if self.board[r][c] == sign and self.board[r][c + 1] == sign and self.board[r][c + 2] == sign\
                        and self.board[r][c + 3] == sign and self.board[r][c + 4] == sign:
                    return True
        # vertical
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 4):
                if self.board[r][c] == sign and self.board[r + 1][c] == sign and self.board[r + 2][c] == sign\
                        and self.board[r + 3][c] == sign and self.board[r + 4][c] == sign:
                    return True
        # diagonal+
        for c in range(0, COLUMN_COUNT - 4):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == sign and self.board[r - 1][c + 1] == sign and self.board[r - 2][c + 2] == sign\
                        and self.board[r - 3][c + 3] == sign and self.board[r - 4][c + 4] == sign:
                    return True
        # diagonal-
        for c in range(0, COLUMN_COUNT - 4):
            for r in range(0, ROW_COUNT - 4):
                if self.board[r][c] == sign and self.board[r + 1][c + 1] == sign and self.board[r + 2][c + 2] == sign\
                        and self.board[r + 3][c + 3] == sign and self.board[r + 4][c + 4] == sign:
                    return True


class Screen:
    def __init__(self, title, w=COLUMN_COUNT * SIZE, h=(COLUMN_COUNT+1) * SIZE):
        self.title = title
        self.w = w
        self.h = h
        self.current = False

    def make_current(self):
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode((self.w, self.h))

    def not_current(self):
        self.current = False

    def get_screen(self):
        return self.screen

    def update(self):
        if self.current:
            self.screen.fill(BLACK)


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
        pygame.draw.rect(self.window, WHITE, (self.x, self.y, self.w, self.h))
        self.window.blit(self.font.render(str(self.i+1), False, BLACK), (self.x + 10, self.y - 10))

    def draw_text(self, text):
        pygame.draw.rect(self.window, WHITE, (self.x, self.y, self.w, self.h))
        self.window.blit(self.font.render(text, False, BLACK), (self.x + 10, self.y - 5))

    def get_pos(self):
        return self.x, self.y


def main():
    pygame.init()
    pygame.font.init()
    game_over = False
    turn = 0
    screen_basic = Screen("Connect four")
    screen_winning = Screen("WINNER!!!")
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    otherfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen_winning.make_current()
    screen_win = screen_winning.get_screen()
    screen_basic.make_current()
    screen = screen_basic.get_screen()
    mode = FourInRow(screen, myfont, otherfont)
    column_buttons = []
    reset_button = Button(20, 717, 150, 50, myfont, screen_win)
    reset_button.draw_text("RESET")
    pygame.draw.rect(screen, BLUE, (198, 702, 174, 44,))
    four_in_button = Button(200, 704, 170, 40, otherfont, screen_win)
    four_in_button.draw_text("4 IN ROW")
    five_in_button = Button(200, 748, 170, 40, otherfont, screen_win)
    five_in_button.draw_text("5 IN ROW")
    x = 25
    y = 25
    for i in range(0, COLUMN_COUNT):
        column_buttons.append(Button(x, y, 50, 50, myfont, screen, i))
        column_buttons[i].draw()
        x += 100
        pygame.display.update()
        text = myfont.render('Player 1 turn', True, YELLOW)
        screen.blit(text, (400, 700))
    print(mode.create_board())
    mode.draw_board()
    board = mode.get_board()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if mode.selected_mode(170, 40, five_in_button, four_in_button, "5 IN ROW", "4 IN ROW"):
                    mode = FiveInRow(screen, myfont, otherfont, board)
                    turn = 0
                elif mode.selected_mode(170, 40, four_in_button, five_in_button, "4 IN ROW", "5 IN ROW"):
                    mode = FourInRow(screen, myfont, otherfont, board)
                    turn = 0
                if mode.button_pressed(150, 50, reset_button):
                    turn = mode.reset()
                for i in range(0, COLUMN_COUNT):
                    if mode.button_pressed(50, 50, column_buttons[i]):
                        if turn == 0:
                            col = int(math.floor(event.pos[0] / SIZE))
                            if mode.correct_location(col):
                                pygame.draw.rect(screen, BLACK, (400, 700, 500, 500))
                                text = myfont.render('Player 2 turn', True, YELLOW)
                                screen.blit(text, (400, 700))
                                row = mode.next_free_space(col)
                                mode.drop(col, row, 1)
                                if mode.winning_check(1):
                                    screen_winning.make_current()
                                    screen_basic.not_current()
                                    screen_winning.update()
                                    mode.won(0)
                                    pygame.display.update()
                                    print("Player 1 Wins")
                                    game_over = True
                                    mode = FourInRow(screen, myfont, otherfont, board)
                                turn += 1
                                turn = turn % 2
                        else:
                            col = int(math.floor(event.pos[0] / SIZE))
                            if mode.correct_location(col):
                                pygame.draw.rect(screen, BLACK, (400, 700, 500, 500))
                                text = myfont.render('Player 1 turn', True, YELLOW)
                                screen.blit(text, (400, 700))
                                row = mode.next_free_space(col)
                                mode.drop(col, row, 2)
                                if mode.winning_check(2):
                                    screen_winning.make_current()
                                    screen_basic.not_current()
                                    screen_winning.update()
                                    mode.won(1)
                                    pygame.display.update()
                                    print("Player 2 Wins")
                                    game_over = True
                                    mode = FourInRow(screen, myfont, otherfont, board)
                                turn += 1
                                turn = turn % 2
                        print(board)
                        if screen_basic.current:
                            mode.draw_board()
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                screen_basic.make_current()
                screen_winning.not_current()
                screen_basic.update()
                turn = mode.reset()
                game_over = False
                for i in range(0, COLUMN_COUNT):
                    column_buttons[i].draw()
                reset_button.draw_text("RESET")
                pygame.draw.rect(screen, BLUE, (198, 702, 174, 44,))
                four_in_button.draw_text("4 IN ROW")
                five_in_button.draw_text("5 IN ROW")
                mode.draw_board()
                pygame.display.update()


if __name__ == "__main__":
    main()
