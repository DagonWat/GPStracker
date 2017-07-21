#import pygame_sdl2
#pygame_sdl2.import_as_pygame()

import pygame
import os

def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    sleeping = False

    font = pygame.font.Font("DejaVuSans.ttf", 24)
    text = font.render("Seriy Petyh.", True, (255, 255, 255, 255))
    text_w, text_h = text.get_size()

    clicked = False
    click_x = 0
    click_y = 0

    while True:

        ev = pygame.event.wait()

        if not sleeping:
            screen.fill((0, 0, 0, 255))

            if clicked:
                screen.blit(text, (960 + (pygame.mouse.get_pos()[0] - click_x), 540 + (pygame.mouse.get_pos()[1] - click_y)))

            else:
                screen.blit(text, (960 , 540))

            pygame.display.flip()

        ev = pygame.event.wait()

        if ev.type == pygame.QUIT:
            break

        elif ev.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            click_x, click_y = ev.pos

        elif ev.type == pygame.MOUSEBUTTONUP:
            clicked = False

if __name__ == "__main__":
    main()
