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
fontCapture = pygame.font.Font(os.path.join("fonts", "Capture_it.ttf"), 28)

def main():
    screen = pygame.display.set_mode((screenX, screenY))

    sleeping = False
    clicked = False

    click_x = 0
    click_y = 0

    player1 = []
    player2 = []
    soldiers = []

    heroes = [soldier, horse, tevton]
    players = [player1, player2]
    players_gex = [player1_gex, player2_gex]

    memory = [10000, 10000]

    turn = 0


    pull1 =  5
    pull2 =  5
    pulls = [pull1, pull2]

    for i in range(50):
        soldiers.append(0)
        player1.append(0)
        player2.append(0)



    screen.fill((GREEN))
    screen.blit(web, (0, 0))

    while True:

        if not sleeping:

            if clicked:

                if turn < 50:

                    for i in range(0, 50):

                        if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2:

                            if turn < 49 and player1[i] == 0 and player2[i] == 0:

                                screen.blit(green_gex, (memory[0] - green_gex.get_width() / 2, memory[1] - green_gex.get_height() / 2))
                                screen.blit(players_gex[(turn + 1) % 2], (memory[0] - player2_gex.get_width() / 2, memory[1] - player2_gex.get_height() / 2))

                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(circle, (web_list[i][0] - circle.get_width() / 2, web_list[i][1] - circle.get_height() / 2))
                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                memory = [web_list[i][0], web_list[i][1]]

                                players[turn % 2][i] = 1
                                turn += 1
                                clicked = False

                            elif turn == 49:
                                screen.blit(green_gex, (memory[0] - green_gex.get_width() / 2, memory[1] - green_gex.get_height() / 2))
                                screen.blit(players_gex[(turn + 1) % 2], (memory[0] - player2_gex.get_width() / 2, memory[1] - player2_gex.get_height() / 2))

                                players[turn % 2][i] = 1
                                turn += 1

                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(player2_gex, (web_list[i][0] - player2_gex.get_width() / 2, web_list[i][1] - player2_gex.get_height() / 2))

                                clicked = False


                        elif i == 49:
                            clicked = False

                else:

                    for i in range(50):


                        if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2 and players[turn % 2][i] == 1 and pulls[turn % 2] >= 0 :

                            pulls[turn % 2] -= 1
                            screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                            screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                            soldiers[i] += 1

                            clicked = False

                            if turn % 2 == 0:
                                text = fontCapture.render("blue units : " + str(pulls[turn % 2] + 1), True, GREEN)
                                screen.blit(text, (screenX  / 8 - text.get_width() / 2 + 45, 0))
                                text = fontCapture.render("blue units : " + str(pulls[turn % 2]), True, WHITE)
                                screen.blit(text, (screenX  / 8  - text.get_width() / 2 + 45, 0))

                            else:
                                text = fontCapture.render("red units : " + str(pulls[turn % 2] + 1), True, GREEN)
                                screen.blit(text, (screenX  / 8 * 7 - text.get_width() / 2 - 50, 0))
                                text = fontCapture.render("red units : " + str(pulls[turn % 2]), True, WHITE)
                                screen.blit(text, (screenX  / 8 * 7  - text.get_width() / 2 - 50, 0))

                            if pulls[turn % 2] == 0:

                                turn += 1

                            if pulls[turn % 2] == 0 and  pulls[(turn + 1) % 2] == 0 :

                                pull1 =  2 + round(0.1*player1.count(1)) + turn - 50
                                pull2 =  2 + round(0.1*player2.count(1)) + turn - 50
                                pulls = [pull1, pull2]


            for i in range(50):

                if (soldiers[i] > 0 and soldiers[i] < 45):

                    for j in range(((soldiers[i] - soldiers[i] // 15 * 15) // 5) + 1):

                        screen.blit(heroes[soldiers[i] // 15], \
                        (web_list[i][0] - heroes[soldiers[i] // 15].get_width() / 2 - j * 10, web_list[i][1] - heroes[soldiers[i] // 15].get_height() / 2 + j * 5))

                    text = fontCapture.render(str(soldiers[i]), True, (255, 255, 255, 255))
                    screen.blit(text, (web_list[i][0] -15, web_list[i][1]- 70))

            if turn % 2 == 0:
                text = fontCapture.render("player 2", True, GREEN)
                screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                text = fontCapture.render("player 1", True, WHITE)
                screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

            else:
                text = fontCapture.render("player 1", True, GREEN)
                screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                text = fontCapture.render("player 2", True, WHITE)
                screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

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
