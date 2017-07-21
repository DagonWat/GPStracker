import pygame_sdl2
pygame_sdl2.import_as_pygame()

import pygame
import os

def main():
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    sleeping = False

    font = pygame.font.Font("DejaVuSans.ttf", 24)
    text = font.render("Seriy Petyh.", True, (255, 255, 255, 255))
    text_w, text_h = text.get_size()

    clicked = False
    click_x = 0
    click_y = 0

    new_x = 960
    new_y = 540

    while True:

        ev = pygame.event.wait()

        if not sleeping:
            screen.fill((0, 0, 0, 255))

            while clicked:

                screen.fill((0, 0, 0, 255))
                screen.blit(text, (new_x + (pygame.mouse.get_pos()[0] - click_x), new_y + (pygame.mouse.get_pos()[1] - click_y)))
                pygame.display.flip()

                ev = pygame.event.wait()

                if ev.type == pygame.MOUSEBUTTONUP:
                    clicked = False
                    new_x = new_x + (pygame.mouse.get_pos()[0] - click_x)
                    new_y = new_y + (pygame.mouse.get_pos()[1] - click_y)

            screen.blit(text, (960 , 540))



        ev = pygame.event.wait()

        if ev.type == pygame.QUIT:
            break

        elif ev.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            click_x, click_y = ev.pos

if __name__ == "__main__":
    main()
