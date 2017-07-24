#import pygame_sdl2
#pygame_sdl2.import_as_pygame()

import pygame, os
from sheets import *
from circles import*

pygame.init()

screenX = 1920
screenY = 1080
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 200,  20)
BLUE  = (  0,   0, 255)
RED   = (255,   0,   0)
GREY  = ( 71,  58,  53)

fontCavier = pygame.font.Font(os.path.join("fonts", "CaviarDreams.ttf"), 24)
fontDeja = pygame.font.Font(os.path.join("fonts", "DejaVuSans.ttf"), 24)

def main():
    screen = pygame.display.set_mode((screenX, screenY))

    sleeping = False
    clicked = False

    text = fontCavier.render("Seriy Petyh.", True, (255, 255, 255, 255))

    click_x = 0
    click_y = 0

    circleX = 10000
    circleY = 10000

    player1 = []
    player2 = []

    soldiers = []
    for i in range(50):
        soldiers.append(0)


    turn = 0

    screen.fill((GREEN))
    screen.blit(web, (0, 0))

    while True:

        if not sleeping:

            while clicked:

                for i in range(0, 50):

                    if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2:

                        turn += 1

                        circleX = web_list[i][0]
                        circleY = web_list[i][1]

                        if turn % 2 == 0 :
                            player1.append((circleX - your_gex.get_width() / 2, circleY - your_gex.get_height() / 2))
                            clicked = False
                            break

                        else :
                            player2.append((circleX - enemy_gex.get_width() / 2, circleY - enemy_gex.get_height() / 2))
                            clicked = False
                            break

                        if turn >= 50:
                            soldiers[i] += 1


                    elif (i == 49):
                        clicked = False

            for i in range(50):
                if soldiers[i] != 0:
                    screen.blit(soldier, web_list[i])

            for i in range(len(player1)):

                screen.blit(your_gex, player1[i])

            for i in range(len(player2)):

                screen.blit(enemy_gex, player2[i])

            screen.blit(circle, (circleX - circle.get_width() / 2, circleY - circle.get_height() / 2))

            pygame.display.flip()

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()
                break

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                click_x, click_y = ev.pos


if __name__ == "__main__":
    main()

#python android.py --launch build /home/egor/ProjectA release install
