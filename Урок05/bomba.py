import os
import random
import sys

import pygame


pygame.init()
size = width, height = 1500, 1000
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png", colorkey=-1)
    image_boom = load_image("boom.jpg", colorkey=-1)
    image_boom = pygame.transform.scale(image_boom, (20, 20))

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)
        self.life = 200
        self.count = 0

    def update(self, *args):
        self.life += self.count
        self.rect = self.rect.move(random.randrange(25) - 11,
                                   random.randrange(25) - 11)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom
            self.count = -1
        if self.life < 0:
            self.kill()


all_sprites = pygame.sprite.Group()

for _ in range(5000):
    Bomb(all_sprites)

running = True
clock = pygame.time.Clock()

fps = 100
ext_event = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:

        #     if event.button == 1:
        #         board.get_click(event.pos)
        #     if event.button == 3:
        #         board.set_life()
        #     if event.button == 4:
        #         step = max(10, step - 1)
        #     if event.button == 5:
        #         step += 1
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     board.set_life()
        all_sprites.update(event)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
