import pygame


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

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x, line in enumerate(self.board):
            for y, cell in enumerate(line):
                screen.fill(cw, (self.left + y * self.cell_size,
                                 self.top + x * self.cell_size,
                                 self.cell_size, self.cell_size))
                if cell == 0:
                    screen.fill(cb, (self.left + y * self.cell_size + 1,
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

pygame.init()
size = width, heigt = (800, 600)
screen = pygame.display.set_mode(size)
cw = pygame.Color('white')
cb = pygame.Color('black')
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)

    pygame.display.flip()
pygame.quit()
