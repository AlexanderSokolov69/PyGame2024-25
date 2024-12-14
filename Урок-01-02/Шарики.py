import pygame


def draw(screen, pos):
    pygame.draw.circle(screen, 'white', pos, 10)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шарики')
    clock = pygame.time.Clock()
    fps = 100
    count = 0
    balls = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append([*event.pos, -1, -1])

        screen.fill('black')
        for i, (x, y, dx, dy) in enumerate(balls):
            draw(screen, (x, y))
            x += dx
            y += dy
            if x < 10 or x > width - 10:
                dx *= -1
            if y < 10 or y > height - 10:
                dy *= -1
            balls[i] = [x, y, dx, dy]
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
