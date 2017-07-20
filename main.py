import pygame_sdl2
pygame_sdl2.import_as_pygame()

import pygame
import os

def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    sleeping = False

    font = pygame.font.Font("DejaVuSans.ttf", 24)
    text = font.render("Seriy Petyh.", True, (255, 255, 255, 255))
    text_w, text_h = text.get_size()

    while True:

        if not sleeping:
            screen.fill((0, 0, 0, 255))

            screen.blit(text, (960, 540))

            pygame.display.flip()

        ev = pygame.event.wait()

        if ev.type == pygame.QUIT:
            break

if __name__ == "__main__":
    main()
