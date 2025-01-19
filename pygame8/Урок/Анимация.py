import os
import sys
import random

import pygame

pygame.init()
size = WIDTH, HEIGHT = 800, 600
GRAVITY = 0.1
screen_rect = (0, 0, WIDTH, HEIGHT)
clock = pygame.time.Clock()
fps = 50
screen = pygame.display.set_mode(size)

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image

all_sprites = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.move = {'up': 0, 'left': 1, 'down': 2, 'right': 3}
        self.columns = columns
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.count = 4
        self.frame = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        print(len(self.frames))

    def update(self):
        keys = pygame.key.get_pressed()
        move = None
        if  keys[pygame.K_LEFT]:
            move = 'left'
            self.rect.x -= 2
        elif  keys[pygame.K_RIGHT]:
            move = 'right'
            self.rect.x += 2
        elif  keys[pygame.K_UP]:
            move = 'up'
            self.rect.y -= 2
        elif  keys[pygame.K_DOWN]:
            move = 'down'
            self.rect.y += 2
        if move:
            self.frame += 1
            if self.count < self.frame:
                self.frame = 0
                self.cur_frame = ((self.cur_frame + 1) % self.columns)
                print(self.cur_frame, self.cur_frame + self.move[move] * self.columns)
                self.image = pygame.transform.scale(self.frames[self.cur_frame + self.move[move] * self.columns],
                                                    (100, 100))


# для отслеживания улетевших частиц
# удобно использовать пересечение прямоугольников


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(Particle.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()

def create_particles(position):
    # количество создаваемых частиц
    particle_count = 200
    # возможные скорости
    numbers = range(-3, 4)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), 10 * random.choice(numbers))


if __name__ == "__main__":
#    dragon = AnimatedSprite(load_image("dragon_sheet8x2.png"), 8, 2, 50, 50)
    pups = AnimatedSprite(load_image('pups.jpg'), 9, 4, 200, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                create_particles(event.pos)

        all_sprites.update()
        screen.fill('black')
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(fps)
