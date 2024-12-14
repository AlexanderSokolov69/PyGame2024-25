import pygame

try:
    size = [int(x) for x in input().split()]
    if len(size) != 2:
        raise ValueError
except Exception as e:
    print("Неправильный формат ввода")
pygame.init()
screen = pygame.display.set_mode(size)
c_white = pygame.Color('white')
pygame.draw.line(screen, c_white, (0, 0), size, width=5)
pygame.draw.line(screen, c_white, (0, size[1]), (size[0], 0), width=5)
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()
