#import pygame_sdl2
#pygame_sdl2.import_as_pygame()

import pygame, os, time, math
from sheets import *
from circles import *
from amount import *

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

screen = pygame.display.set_mode((screenX, screenY))

def main():

    sleeping = False
    clicked = False
    holding = False

    click_x = 0
    click_y = 0

    click_time = 0

    turn = 30
    am = 1

    pointers = []

    player1 = []
    player2 = []
    soldiers = []
    pull1 =  5
    pull2 =  5

    heroes = [soldier, horse, tevton]
    players = [player1, player2]
    players_gex = [player1_gex, player2_gex]
    pulls = [pull2, pull1]
    arrows = [[[green_up, red_up, -20, -100], [green_down, red_down, -20, 50]], \
                [[green_up_left, red_up_left, -75, -50], [green_down_left, red_down_left, -77, 20]], \
                [[green_up_right, red_up_right, 40, -50], [green_down_right, red_down_right, 35, 20]]]
    memory = [10000, 10000]

    for i in range(50):
        soldiers.append(0)
        player1.append(0)
        player2.append(0)

    screen.fill((GREEN))
    screen.blit(web, (0, 0))
    screen.blit(turn_bttn, (screenX / 2 - turn_bttn.get_width() / 2 - 8, 30))

    while True:

        if (not sleeping):

            if (clicked):

                if (turn < 50):

                    for i in range(50):

                        if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2:

                            if turn < 49 and player1[i] + player2[i] == 0:

                                screen.blit(green_gex, (memory[0] - green_gex.get_width() / 2, memory[1] - green_gex.get_height() / 2))
                                screen.blit(players_gex[(turn + 1) % 2], (memory[0] - players_gex[(turn + 1) % 2].get_width() / 2, memory[1] - players_gex[(turn + 1) % 2].get_height() / 2))

                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(circle, (web_list[i][0] - circle.get_width() / 2, web_list[i][1] - circle.get_height() / 2))
                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                memory = [web_list[i][0], web_list[i][1]]

                                players[turn % 2][i] = 1
                                turn += 1
                                clicked = False

                            elif turn == 49 and player1[i] + player2[i] == 0:
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

                    if (not holding):

                        if click_x >= screenX / 2 - turn_bttn.get_width() / 2 - 8 and click_x <= screenX / 2 + turn_bttn.get_width() / 2 + 8 \
                            and click_y >= 30 and click_y <= 30 + turn_bttn.get_height():

                            if (players[turn % 2].count(1) - 24 > 0):
                                pulls[turn % 2] += int(2 + abs(players[turn % 2].count(1) - 24) + turn - 50)

                            else:
                                pulls[turn % 2] += int(2 + round(0.1 * players[turn % 2].count(1)) + turn - 50)

                            turn += 1
                            clicked = False

                        if pulls[(turn + 1) % 2] == 0:

                            pulls[(turn + 1) % 2] = int(2 + round(0.1 * players[(turn + 1) / 2].count(1)) + turn - 50)

                        for i in range(50):

                            if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2 and players[turn % 2][i] == 1 and pulls[turn % 2] > 0 :

                                pulls[turn % 2] -= am

                                if pulls[turn % 2] < 0:
                                    am = am + pulls[turn % 2]
                                    pulls[turn % 2] = 0

                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                soldiers[i] += am

                                clicked = False

                                break

                        screen.blit(green_gex, (280 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("blue : " + str(pulls[0]), True, WHITE)
                        screen.blit(text, (screenX  / 8  - text.get_width() / 2 + 45, 0))

                        screen.blit(green_gex, (1624 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("red : " + str(pulls[1]), True, WHITE)
                        screen.blit(text, (screenX  / 8 * 7  - text.get_width() / 2 - 50, 0))

                        am = int(amount(screen, click_x, click_y, button_x1, button_x5, button_x10))
                        clicked = False

                    elif (time.time() - click_time > 1):

                        for i in range(50):

                            if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2 and players[turn % 2][i] == 1 and soldiers[i] != 0:
                                clicked = False
                                pointers = []

                                for j in range (50):
                                    if (web_list[i][0] - web_list[j][0]) ** 2 + (web_list[i][1] - web_list[j][1]) ** 2 < 230 ** 2:
                                        pointers.append(j)

                                for j in range(len(pointers)):
                                    if players[turn % 2][pointers[j]] == 1 and pointers[j] != i:

                                        a = int((web_list[i][0] - web_list[pointers[j]][0]) / 168)
                                        b = ((web_list[i][1] - web_list[pointers[j]][1]) / 216)
                                        if b == 0.0:
                                            b = int(0)
                                        if b == 1.0:
                                            b = int(0)
                                        if b == -1.0:
                                            b = int(1)
                                        if b == 0.5:
                                            b = int(0)
                                        if b == - 0.5:
                                            b = int(1)

                                        screen.blit(arrows[a][b][0], (web_list[i][0] + arrows[a][b][2], web_list[i][1] + arrows[a][b][3]))
                                    if players[(turn+1) % 2][pointers[j]] == 1 and pointers[j] != i:
                                        a = int((web_list[i][0] - web_list[pointers[j]][0]) / 168)
                                        b = ((web_list[i][1] - web_list[pointers[j]][1]) / 216)
                                        if b == 0.0:
                                            b = int(0)
                                        if b == 1.0:
                                            b = int(0)
                                        if b == -1.0:
                                            b = int(1)
                                        if b == 0.5:
                                            b = int(0)
                                        if b == - 0.5:
                                            b = int(1)

                                        screen.blit(arrows[a][b][1], (web_list[i][0] + arrows[a][b][2], web_list[i][1] + arrows[a][b][3]))


                                pygame.display.flip()

                                while (clicked == False):

                                    for ev in pygame.event.get():

                                        if ev.type == pygame.MOUSEBUTTONDOWN:
                                            clicked = True
                                            click_x, click_y = ev.pos

                                for j in range(50):

                                    if (web_list[j][0] - click_x) ** 2 + (web_list[j][1] - click_y) ** 2 < R ** 2:

                                        a = math.sqrt((web_list[i][0] - web_list[j][0])**2 + (web_list[i][1] - web_list[j][1])**2)

                                        if a <= 230 and web_list[j] !=  web_list[i]:

                                            if players[turn % 2][j] == 1:

                                                soldiers[i] -= am

                                                if soldiers[i] <= 0:
                                                    am = am + soldiers[i]
                                                    soldiers[i] = 0
                                                    screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                                    screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                                soldiers[j] += am
                                                am = 1

                                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))
                                                screen.blit(green_gex, (web_list[j][0] - green_gex.get_width() / 2, web_list[j][1] - green_gex.get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[j][0] - players_gex[turn % 2].get_width() / 2, web_list[j][1] - players_gex[turn % 2].get_height() / 2))

                                            if players[(turn + 1) % 2][j] == 1:

                                                print("attack")

                        clicked = False

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

            elif ev.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                click_time = time.time()
                clicked = True
                holding = True
                click_x, click_y = ev.pos

            elif (ev.type == pygame.MOUSEBUTTONUP):
                holding = False

if __name__ == "__main__":
    main()

#python android.py --launch build /home/egor/ProjectA release install
