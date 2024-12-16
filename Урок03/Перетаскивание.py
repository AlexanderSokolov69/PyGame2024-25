import pygame

pygame.init()
size = width, heigt = (300, 300)
screen = pygame.display.set_mode(size)
cg = pygame.Color('green')
rx = 0
ry = 0
rsize = 100
fmove = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            fmove = True
        if event.type == pygame.MOUSEBUTTONUP:
            fmove = False
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
            if fmove:
                rx += event.rel[0]
                ry += event.rel[1]
    screen.fill((0, 0, 0))
    screen.fill(cg, (rx, ry, rsize, rsize))
    pygame.display.flip()
pygame.quit()
