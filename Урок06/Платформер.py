import os
import random
import sys

import pygame


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 50

all_sprites = pygame.sprite.Group()
boards_sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill(pygame.Color('blue'))
        self.rect = self.image.get_rect()
        self.rect.x = width + 1
        self.rect.y = height + 1

    def move(self, *args):
        old_x = self.rect.x
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and args[0].button == 3:
            self.rect.x = args[0].pos[0]
            self.rect.y = args[0].pos[1]
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_LEFT:
                self.rect.x -= 10
            if args[0].key == pygame.K_RIGHT:
                self.rect.x += 10
        if pygame.sprite.spritecollideany(self, boards_sprites):
            self.rect.x = old_x

    def update(self):
        old_y = self.rect.y
        if not pygame.sprite.spritecollideany(self, boards_sprites):
            self.rect.y += 50 / fps
        if pygame.sprite.spritecollideany(self, boards_sprites):
            self.rect.y = old_y


class Board(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(boards_sprites, all_sprites)
        self.image = pygame.surface.Surface((50, 10))
        self.image.fill(pygame.Color('gray'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


player = Player()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.move(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.move(event)
            if event.button == 1:
                Board(event.pos)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.set_caption(f'{player.rect.x}, {player.rect.y}')
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
