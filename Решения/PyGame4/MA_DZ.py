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
        self.cr = pygame.Color('red')
        self.cbl = pygame.Color('blue')
        self.r = False
        self.rk = 0, 0

    def on_click(self, cell_coords):
        if not cell_coords:
            return
        x, y = cell_coords
        if not self.r:
            if self.board[y][x] == 0:
                self.board[y][x] += 1
            elif self.board[y][x] == 1:
                self.board[y][x] = 2
                self.r = True
                self.rk = x, y
        elif self.r and self.board[y][x] == 0:
            a = self.has_path(x, y, *self.rk)
            if a:
                self.r = False
                self.board[y][x] = 1
                self.board[self.rk[1]][self.rk[0]] = 0


    def render(self, screen):
        for x, line in enumerate(self.board):
            for y, cell in enumerate(line):
                screen.fill(self.cw, (self.left + y * self.cell_size, self.top + x * self.cell_size, self.cell_size, self.cell_size))
                screen.fill(self.cb, (self.left + y * self.cell_size + 1, self.top + x * self.cell_size + 1, self.cell_size - 2, self.cell_size - 2))
                if cell == 1:
                    pygame.draw.circle(screen, self.cbl, (self.left + y * self.cell_size + self.cell_size // 2, self.top + x * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 1, 0)
                elif cell == 2:
                    pygame.draw.circle(screen, self.cr, (self.left + y * self.cell_size + self.cell_size // 2, self.top + x * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 1, 0)

    def has_path(self, x1, y1, x2, y2):
        def get_state(x, y):
            if x < 0 or y < 0 or self.height <= y or self.width <= x:
                return False
            return True
        a = x1, y1
        d = set()
        d.add(a)
        d1 = set()
        while d != d1:
            d1 = d.copy()
            d = set()
            for i in d1:
                x, y = i[0], i[1]
                if get_state(x, y + 1) and self.board[y + 1][x] != 1:
                    d.add((x, y + 1))
                if  get_state(x, y - 1) and self.board[y - 1][x] != 1:
                    d.add((x, y - 1))
                if get_state(x + 1, y) and self.board[y][x + 1] != 1:
                    d.add((x + 1, y))
                if get_state(x - 1, y) and self.board[y][x - 1] != 1:
                    d.add((x - 1, y))
                d.add(i)
        a = x2, y2
        if a in d1:
            return True
        return False



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
