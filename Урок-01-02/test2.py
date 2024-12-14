import pygame
import random


def draw(screen, count):
    # screen.fill('black')
    pygame.draw.circle(screen, 'red', (int(count), screen.get_height() // 2), 50)
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 50
    v = 100
    count = 0
    point = (0, 0)
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        draw(screen, count)
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                point = event.pos
        # отрисовка и изменение свойств объектов

        pygame.draw.circle(screen, (0, 0, 255), point, 20)
        # обновление экрана
        pygame.display.flip()
        count = (count + v * fps / 1000) % width
        clock.tick(fps)
    pygame.quit()
