import pygame


def draw(screen, count, pos):
    pygame.draw.circle(screen, 'yellow', pos, count)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 100
    count = 0
    pos = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                count = 0

        screen.fill('blue')
        if pos:
            draw(screen, count, pos)
            count += 1
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
