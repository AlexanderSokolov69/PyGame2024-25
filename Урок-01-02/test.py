import pygame
import random


def draw(screen, shift):
    c_black = pygame.Color(0, 0, 0)
    screen.fill(c_black, (100, 100, 600, 400))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (100, 255, 100))
    text_x = screen.get_width() // 2 - text.get_width() // 2
    text_y = screen.get_height() // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x + shift, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    scr = pygame.display.set_mode(size)
    shift = 0

    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        draw(scr, shift)
        pygame.display.flip()
        shift += 1


    # завершение работы:
    pygame.quit()
