import pygame
import copy
from random import randint


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.cb = pygame.Color('black')
        self.cw = pygame.Color('white')

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x, line in enumerate(self.board):
            for y, cell in enumerate(line):
                screen.fill(self.cw, (self.left + y * self.cell_size, self.top + x * self.cell_size, self.cell_size, self.cell_size))
                if cell == 0:
                    screen.fill(self.cb, (self.left + y * self.cell_size + 1, self.top + x * self.cell_size + 1, self.cell_size - 2, self.cell_size - 2))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        lx = (mouse_pos[0] - self.left) // self.cell_size
        ly = (mouse_pos[1] - self.top) // self.cell_size
        if (0 <= lx < self.width) and (0 <= ly < self.height):
            return lx, ly


    def on_click(self, cell_coords):
        cells = set()
        for x in range(self.width):
            cells.add((x, cell_coords[1]))
        for y in range(self.height):
            cells.add((cell_coords[0], y))
        for cell in cells:
            self.invert(cell)

    def invert(self, cell_coords):
        self.board[cell_coords[1]][cell_coords[0]] = not self.board[cell_coords[1]][cell_coords[0]]

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Lines(Board):
    def __init__(self, x=10, y=10):
        super().__init__(x, y, cell_size=40)
        self.board = [[0] * x for _ in range(y)]
        for i in range(x):
            for j in range(y):
                self.board[j][i] = randint(1, 2)
        self.cr = pygame.Color('red')
        self.cbl = pygame.Color('blue')
        self.h = 1

    def on_click(self, cell_coords):
        x, y = cell_coords
        if self.board[y][x] == self.h + 1:
            self.invert(self.h, x, y)
            self.h = not self.h


    def render(self, screen):
        for x, line in enumerate(self.board):
            for y, cell in enumerate(line):
                screen.fill(self.cw, (self.left + y * self.cell_size, self.top + x * self.cell_size, self.cell_size, self.cell_size))
                screen.fill(self.cb, (self.left + y * self.cell_size + 1, self.top + x * self.cell_size + 1, self.cell_size - 2, self.cell_size - 2))
                if cell == 1:
                    pygame.draw.circle(screen, self.cbl, (self.left + y * self.cell_size + self.cell_size // 2, self.top + x * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 1, 0)
                elif cell == 2:
                    pygame.draw.circle(screen, self.cr, (self.left + y * self.cell_size + self.cell_size // 2, self.top + x * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 1, 0)

    def invert(self, h, x, y):
        for i in range(self.width):
            self.board[i][x] = h + 1
        for i in range(self.height):
            self.board[y][i] = h + 1


pygame.init()
size = (420, 420)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Линеечки')
board = Lines()
running = True
clock = pygame.time.Clock()
fps = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
    screen.fill((0, 0, 0))

    board.render(screen)

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()