import os
import sys

import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

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


pygame.mouse.set_visible(False)
pygame.display.set_caption('Герой двигается!')
running = True
clock = pygame.time.Clock()
fps = 10
all_sprits = pygame.sprite.Group()
hero = pygame.sprite.Sprite(all_sprits)
hero.image = load_image('creature.png')
hero.rect = hero.image.get_rect()
hero.rect.x = 0
hero.rect.y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.rect.x -= 10
        hero.rect.x %= width - hero.rect.width
    if keys[pygame.K_RIGHT]:
        hero.rect.x += 10
        hero.rect.x %= width - hero.rect.width
    if keys[pygame.K_UP]:
        hero.rect.y -= 10
        hero.rect.y %= height - hero.rect.height
    if keys[pygame.K_DOWN]:
        hero.rect.y += 10
        hero.rect.y %= height - hero.rect.height
    screen.fill((255, 255, 255))
    all_sprits.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()