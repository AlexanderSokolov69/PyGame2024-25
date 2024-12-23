import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
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


all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("bomb.png")
# и размеры
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 5
sprite.rect.y = 20
# добавим спрайт в группу
all_sprites.add(sprite)

running = True
clock = pygame.time.Clock()
fps = 100
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

    screen.fill((255, 0, 0))
    img = load_image('Sprite.jpg', colorkey=(pygame.Color('white')))
    coef = img.get_height() / screen.get_height()
    img = pygame.transform.scale(img, (img.get_width() // coef, img.get_height() // coef))
    screen.blit(img, (0, 0))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
