import copy
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


class Life(Board):
    def __init__(self):
        super().__init__(30, 30, left=10, top=10, cell_size=20)
        self.cg = pygame.Color('green')
        self.life = False

    def set_life(self):
        self.life = not self.life
        return self.life

    def on_click(self, cell_coord):
        if not self.life:
            self.invert(cell_coord)

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
                else:
                    screen.fill(self.cg, (self.left + y * self.cell_size + 1,
                                          self.top + x * self.cell_size + 1,
                                          self.cell_size - 2, self.cell_size - 2))

    def next_move(self):
        def get_state(x, y):
            x %= self.width
            y %= self.height
            return self.board[y][x]

        if self.life:
            new_board = copy.deepcopy(self.board)
            for x in range(self.width):
                for y in range(self.height):
                    st = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            st += get_state(x + dx, y + dy)
                    st -= get_state(x, y)
                    if st == 3:
                        new_board[y][x] = 1
                    elif st != 2:
                        new_board[y][x] = 0

            self.board = new_board





pygame.init()
size = width, heigt = (620, 620)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Жизнь')
board = Life()
running = True
life = False
clock = pygame.time.Clock()
fps = 100
step = 40
d_step = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
            if event.button == 3:
                board.set_life()
            if event.button == 4:
                step = max(10, step - 1)
            if event.button == 5:
                step += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            board.set_life()

    if d_step > step:
        board.next_move()
        d_step = 0
    screen.fill((0, 0, 0))
    board.render(screen)

    pygame.display.flip()
    clock.tick(fps)
    d_step += 1
pygame.quit()
