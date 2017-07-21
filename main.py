#import pygame_sdl2
#pygame_sdl2.import_as_pygame()

import pygame, os
from sheets import *

pygame.init()

screenX = 1920
screenY = 1080
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 200,  20)
BLUE  = (  0,   0, 255)
RED   = (255,   0,   0)
GREY  = ( 71,  58,  53)

fontCavier = pygame.font.Font("CaviarDreams.ttf", 24)
fontDeja = pygame.font.Font("DejaVuSans.ttf", 24)

def main():
    screen = pygame.display.set_mode((screenX, screenY))

    sleeping = False
    clicked = False

    text = fontCavier.render("Seriy Petyh.", True, (255, 255, 255, 255))

    click_x = 0
    click_y = 0

    new_x = 0
    new_y = 0

    while True:

        if not sleeping:
            screen.fill((GREEN))

            while clicked:

                screen.fill((GREEN))
                screen.blit(web, (new_x + (pygame.mouse.get_pos()[0] - click_x), new_y + (pygame.mouse.get_pos()[1] - click_y)))

                pygame.display.flip()

                for ev in pygame.event.get():

                    if ev.type == pygame.MOUSEBUTTONUP:
                        clicked = False
                        new_x = new_x + (pygame.mouse.get_pos()[0] - click_x)
                        new_y = new_y + (pygame.mouse.get_pos()[1] - click_y)

            screen.blit(web, (new_x, new_y))

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                break

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                click_x, click_y = ev.pos


if __name__ == "__main__":
    main()
