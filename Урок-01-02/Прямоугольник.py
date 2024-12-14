import pygame

try:
    size = [int(x) for x in input().split()]
    if len(size) != 2:
        raise ValueError
except Exception as e:
    print("Неправильный формат ввода")
pygame.init()
screen = pygame.display.set_mode(size)
c_red = pygame.Color('red')

screen.fill((0, 0, 0))
screen.fill(c_red, (1, 1, size[0] - 2, size[1] - 2))
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()
