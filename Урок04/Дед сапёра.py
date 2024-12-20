import pygame
from random import randint


class Board:
    # создание поля
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.cw = pygame.Color('white')
        self.cb = pygame.Color('black')

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x, line in enumerate(self.board):
            for y, cell in enumerate(line):
                screen.fill(self.cw, (self.left + y * self.cell_size,
                                      self.top + x * self.cell_size,
                                      self.cell_size, self.cell_size))
                if cell == 0:
                    screen.fill(self.cb, (self.left + y * self.cell_size + 1,
                                          self.top + x * self.cell_size + 1,
                                          self.cell_size - 2, self.cell_size - 2))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        lx = (mouse_pos[0] - self.left) // self.cell_size
        ly = (mouse_pos[1] - self.top) // self.cell_size
        if (0 <= lx < self.width) and (0 <= ly < self.height):
            return lx, ly

    def on_click(self, cell_coord):
        cells = set()
        for x in range(self.width):
            cells.add((x, cell_coord[1]))
        for y in range(self.height):
            cells.add((cell_coord[0], y))
        for cell in cells:
            self.invert(cell)

    def invert(self, cell_coord):
        if cell_coord:
            self.board[cell_coord[1]][cell_coord[0]] = not self.board[cell_coord[1]][cell_coord[0]]


class Miner(Board):
    def __init__(self, x=10, y=15, mines=10):
        super().__init__(x, y, cell_size=40)
        self.board = [[-1] * x for _ in range(y)]
        self.cr = pygame.Color('red')
        tmp = set()
        while len(tmp) < mines:
            tmp.add((randint(0, x - 1), randint(0, y - 1)))
        for x, y in tmp:
            self.board[y][x] = 10

    def render(self, screen: pygame.Surface):
        for x, line in enumerate(self.board):
            for y, cell in enumerate(line):
                screen.fill(self.cw, (self.left + y * self.cell_size,
                                      self.top + x * self.cell_size,
                                      self.cell_size, self.cell_size))
                if cell == -1:
                    screen.fill(self.cb, (self.left + y * self.cell_size + 1,
                                          self.top + x * self.cell_size + 1,
                                          self.cell_size - 2, self.cell_size - 2))
                elif cell == 10:
                    screen.fill(self.cr, (self.left + y * self.cell_size + 1,
                                          self.top + x * self.cell_size + 1,
                                          self.cell_size - 2, self.cell_size - 2))
                else:
                    screen.fill(self.cb, (self.left + y * self.cell_size + 1,
                                          self.top + x * self.cell_size + 1,
                                          self.cell_size - 2, self.cell_size - 2))
                    font = pygame.font.Font(None, 40)
                    text = font.render(str(self.board[x][y]), False , self.cw)
                    screen.blit(text, (self.left + y * self.cell_size + 10,
                                self.top + x * self.cell_size + 10))

    def on_click(self, cell_coord):
        if not cell_coord:
            return
        x, y = cell_coord

        def get_state(x, y):
            if 0 <= x < self.width and 0 <= y < self.height:
                return self.board[y][x] == 10
            else:
                return 0

        if self.board[y][x] != 10:
            st = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    st += get_state(x + dx, y + dy)
            self.board[y][x] = st



pygame.init()
size = width, heigt = (520, 620)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Сапёр')
board = Miner()
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
