#import pygame_sdl2
#pygame_sdl2.import_as_pygame()

import pygame, os, time, math, random
from sheets import *
from circles import *
from amount import *

pygame.init()

screenX = 1920
screenY = 1080
slider_x = 930
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 200,  20)
BLUE  = (  0,   0, 255)
RED   = (255,   0,   0)
GREY  = ( 71,  58,  53)

game_start = False

fontCavier = pygame.font.Font(os.path.join("fonts", "CaviarDreams.ttf"), 24)
fontDeja = pygame.font.Font(os.path.join("fonts", "DejaVuSans.ttf"), 64)
fontCapture = pygame.font.Font(os.path.join("fonts", "Capture_it.ttf"), 28)

cloud1 = [0, cloud1_5, cloud1_4, cloud1_3, cloud1_2, cloud1_1, cloud1_6]
cloud2 = [0, cloud2_1, cloud2_2, cloud2_3, cloud2_4, cloud2_5, cloud2_6]
cloud3 = [0, cloud3_1, cloud3_2, cloud3_3, cloud3_4, cloud3_5, cloud3_6]
cloud4 = [0, cloud4_1, cloud4_2, cloud4_3, cloud4_4, cloud4_5, cloud4_6]
grass = [0, grass2, grass3, grass4, grass3, grass4, grass3]
jewslayer = [0, jewslayer1, jewslayer2, jewslayer3, jewslayer2, jewslayer3, jewslayer2]
anim = [plus, sword]

screen = pygame.display.set_mode((screenX, screenY))

song = pygame.mixer.Sound(os.path.join("music", "main_song2.ogg"))
song.set_volume(0)  #0.5
song.play()

def playervsplayer():

    global game_start, web_list, player1, player2, mass, soldiers, turn, heroes, am, pulls
    game_start = True

    sleeping = False
    clicked = False
    holding = False

    click_x = 0
    click_y = 0

    click_time = 0

    turn = 0
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
    arrows = [[0, [green_down, red_down, -20, 50], [green_up, red_up, -20, -100]], \
                [0, [green_up_left, red_up_left, -75, -50], [green_down_left, red_down_left, -77, 20]], \
                [0, [green_up_right, red_up_right, 40, -50], [green_down_right, red_down_right, 35, 20]]]
    av_move = []
    av_attack = []
    memory = -1

    for i in range(50):
        soldiers.append(0)
        player1.append(0)
        player2.append(0)
        av_move.append(0)
        av_attack.append(0)

    screen.fill((GREEN))
    screen.blit(fon, (0, 0))
    screen.blit(web, (0, 0))
    screen.blit(turn_bttn, (screenX / 2 - turn_bttn.get_width() / 2 - 8, 30))
    screen.blit(settings_game_button,(1920 / 2  + 328 - settings_game_button.get_width() / 2, settings_game_button.get_height()/2 ))


    while True:

        if (not sleeping):

            if (clicked):

                if click_x < (1920 / 2  + 328 + settings_game_button.get_width() / 2) and click_x > (1920 / 2  + 328 - settings_game_button.get_width() / 2) and click_y < 1.5*settings_game_button.get_height() and  click_y > 0.5*settings_game_button.get_height():

                    settings()



                if (turn < 50):

                    for i in range(50):

                        if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2:

                            if (turn < 49) and (player1[i] + player2[i] == 0):
                                if (memory >= 0):
                                    screen.blit(mass[memory], (web_list[memory][0] - mass[memory].get_width() / 2 - 3, web_list[memory][1] - mass[memory].get_height() / 2 - 2))
                                    screen.blit(players_gex[(turn + 1) % 2], (web_list[memory][0] - players_gex[(turn + 1) % 2].get_width() / 2, web_list[memory][1] - players_gex[(turn + 1) % 2].get_height() / 2))

                                screen.blit(mass[i], (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(circle, (web_list[i][0] - circle.get_width() / 2, web_list[i][1] - circle.get_height() / 2))
                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                memory = i

                                players[turn % 2][i] = 1
                                turn += 1
                                clicked = False

                            elif (turn == 49) and (player1[i] + player2[i] == 0):
                                screen.blit(mass[memory], (web_list[memory][0] - mass[memory].get_width() / 2, web_list[memory][1] - mass[memory].get_height() / 2))
                                screen.blit(players_gex[(turn + 1) % 2], (web_list[memory][0] - players_gex[(turn + 1) % 2].get_width() / 2, web_list[memory][1] - players_gex[(turn + 1) % 2].get_height() / 2))

                                players[turn % 2][i] = 1
                                turn += 1

                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                screen.blit(player2_gex, (web_list[i][0] - player2_gex.get_width() / 2, web_list[i][1] - player2_gex.get_height() / 2))

                                clicked = False

                        if i == 49:
                            clicked = False

                else:

                    if (not holding):

                        if (click_x >= screenX / 2 - turn_bttn.get_width() / 2 - 8) and (click_x <= screenX / 2 + turn_bttn.get_width() / 2 + 8) \
                            and (click_y >= 30) and (click_y <= 30 + turn_bttn.get_height()) :

                            if (turn % 2 == 1):
                                for i in range(2):
                                    if (players[turn % 2].count(1) - 24 > 0):
                                        pulls[i] += int(2 + abs(players[turn % 2].count(1) - 24) + turn - 50)

                                    else:
                                        pulls[i] += int(2 + round(0.1 * players[turn % 2].count(1)) + turn - 50)

                            for i in range(50):
                                av_move[i] = 0
                                av_attack[i] = 0

                            turn += 1
                            clicked = False

                        for i in range(50):

                            if ((web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2) and (players[turn % 2][i] == 1) and (pulls[turn % 2] > 0) :

                                pulls[turn % 2] -= am

                                if (pulls[turn % 2] < 0):
                                    am = am + pulls[turn % 2]
                                    pulls[turn % 2] = 0

                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                soldiers[i] += am

                                clicked = False

                                break

                        screen.blit(green_gex, (280 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("blue : " + str(pulls[0]), True, WHITE)
                        screen.blit(text, (screenX  / 8  - text.get_width() / 2 + 45, 10))

                        screen.blit(green_gex, (1624 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("red : " + str(pulls[1]), True, WHITE)
                        screen.blit(text, (screenX  / 8 * 7  - text.get_width() / 2 - 50, 10))

                        am = int(amount(screen, click_x, click_y, button_x1, button_x5, button_x10))
                        clicked = False

                    elif (time.time() - click_time > 1):

                        for i in range(50):

                            if ((web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2) and (players[turn % 2][i] == 1) and (soldiers[i] != 0) and ((av_move[i] == 0) or (av_attack[i] == 0)):
                                clicked = False
                                pointers = []

                                for j in range (50):
                                    if ((web_list[i][0] - web_list[j][0]) ** 2 + (web_list[i][1] - web_list[j][1]) ** 2 < 230 ** 2):

                                        if (players[(turn + 1) % 2][j] == 1) and (av_attack[i] != 1):
                                            pointers.append(j)

                                        elif (av_move[i] != 1) and (players[turn % 2][j] == 1):
                                            pointers.append(j)

                                for j in range(len(pointers)):
                                    if (pointers[j] != i):
                                        a = int((web_list[i][0] - web_list[pointers[j]][0]) / 168)
                                        b = int((web_list[i][1] - web_list[pointers[j]][1]) / 108)

                                        znak = anim[players[(turn+1) % 2][pointers[j]] == 1]

                                        screen.blit(arrows[a][b][players[(turn+1) % 2][pointers[j]] == 1], (web_list[i][0] + arrows[a][b][2], web_list[i][1] + arrows[a][b][3]))
                                        screen.blit(znak, (web_list[pointers[j]][0] - znak.get_width() / 2, web_list[pointers[j]][1] - znak.get_width() / 2))

                                pygame.display.flip()

                                while (clicked == False):

                                    for ev in pygame.event.get():

                                        if (ev.type == pygame.MOUSEBUTTONDOWN):
                                            clicked = True
                                            click_x, click_y = ev.pos

                                for j in range(len(pointers)):
                                    screen.blit(mass[pointers[j]], (web_list[pointers[j]][0] - mass[pointers[j]].get_width() / 2, web_list[pointers[j]][1] - mass[pointers[j]].get_height() / 2))

                                    if turn % 2 == 0:
                                        screen.blit(players_gex[players[(turn + 1) % 2][pointers[j]] == 1], ((web_list[pointers[j]][0] - player1_gex.get_width() / 2, web_list[pointers[j]][1] - player1_gex.get_height() / 2)))
                                    else:
                                        screen.blit(players_gex[players[turn % 2][pointers[j]] == 1], ((web_list[pointers[j]][0] - player1_gex.get_width() / 2, web_list[pointers[j]][1] - player1_gex.get_height() / 2)))

                                for j in range(50):

                                    if (web_list[j][0] - click_x) ** 2 + (web_list[j][1] - click_y) ** 2 < R ** 2:

                                        a = math.sqrt((web_list[i][0] - web_list[j][0]) ** 2 + (web_list[i][1] - web_list[j][1]) ** 2)

                                        if (a <= 230) and (web_list[j] != web_list[i]):

                                            if (players[turn % 2][j] == 1) and (av_move[i] == 0):

                                                soldiers[j] += soldiers[i]
                                                soldiers[i] = 0

                                                av_move[j] = 1

                                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))
                                                screen.blit(mass[i], (web_list[j][0] - mass[i].get_width() / 2, web_list[j][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[j][0] - players_gex[turn % 2].get_width() / 2, web_list[j][1] - players_gex[turn % 2].get_height() / 2))

                                            elif (players[(turn + 1) % 2][j] == 1) and (av_attack[i] == 0):

                                                s1 = int(round(soldiers[i] * random.uniform(0.4, 0.7)))
                                                s2 = 1 + int(round(soldiers[j] * random.uniform(0.7, 0.9)))

                                                av_attack[i] = 1

                                                soldiers[i] -= s2
                                                soldiers[j] -= s1

                                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))
                                                screen.blit(mass[i], (web_list[j][0] - mass[i].get_width() / 2, web_list[j][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[(turn + 1) % 2], (web_list[j][0] - players_gex[(turn + 1) % 2].get_width() / 2, web_list[j][1] - players_gex[(turn + 1) % 2].get_height() / 2))

                                                if (soldiers[j] <= 0) and (soldiers[i] <= 0):

                                                    soldiers[i] = 0
                                                    soldiers[j] = 0

                                                elif (soldiers[j] <= 0):
                                                    players[(turn + 1) % 2][j] = 0
                                                    players[turn % 2][j] = 1

                                                    screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                                    screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))
                                                    screen.blit(mass[i], (web_list[j][0] - mass[i].get_width() / 2, web_list[j][1] - mass[i].get_height() / 2))
                                                    screen.blit(players_gex[turn % 2], (web_list[j][0] - players_gex[turn % 2].get_width() / 2, web_list[j][1] - players_gex[turn % 2].get_height() / 2))

                                                    av_attack[i] = 0
                                                    av_attack[j] = 1
                                                    av_move[i] = 0
                                                    av_move[j] = 1

                                                    soldiers[j] = soldiers[i]
                                                    soldiers[i] = 0

                                                elif (soldiers[i] <= 0):

                                                    av_attack[i] = 0
                                                    soldiers[i] = 0


                                        screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                        screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                break

                        clicked = False

                for i in range(50):

                    if (soldiers[i] > 0 and soldiers[i] < 45):

                        for j in range(((soldiers[i] - soldiers[i] // 15 * 15) // 5) + 1):

                            screen.blit(heroes[soldiers[i] // 15], \
                            (web_list[i][0] - heroes[soldiers[i] // 15].get_width() / 2 - j * 10  , web_list[i][1] - heroes[soldiers[i] // 15].get_height() / 2 + j * 5))

                        text = fontCapture.render(str(soldiers[i]), True, (255, 255, 255, 255))
                        screen.blit(text, (web_list[i][0] - 15, web_list[i][1] - 70))

                if (turn % 2 == 0):
                    text = fontCapture.render("player 2", True, GREY)
                    screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                    text = fontCapture.render("player 1", True, WHITE)
                    screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

                else:
                    text = fontCapture.render("player 1", True, GREY)
                    screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                    text = fontCapture.render("player 2", True, WHITE)
                    screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

            pygame.display.flip()

        for ev in pygame.event.get():

            if (ev.type == pygame.QUIT):
                pygame.quit()
                break

            elif (ev.type == pygame.MOUSEBUTTONDOWN) and (clicked == False):
                click_time = time.time()
                clicked = True
                holding = True
                click_x, click_y = ev.pos

            elif (ev.type == pygame.MOUSEBUTTONUP):
                holding = False

def playervsbot():

    sleeping = False
    clicked = False
    holding = False

    click_x = 0
    click_y = 0

    click_time = 0

    turn = 0
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
    arrows = [[0, [green_down, red_down, -20, 50], [green_up, red_up, -20, -100]], \
                [0, [green_up_left, red_up_left, -75, -50], [green_down_left, red_down_left, -77, 20]], \
                [0, [green_up_right, red_up_right, 40, -50], [green_down_right, red_down_right, 35, 20]]]
    av_move = []
    av_attack = []
    memory = -1

    for i in range(50):
        soldiers.append(0)
        player1.append(0)
        player2.append(0)
        av_move.append(0)
        av_attack.append(0)

    screen.fill((GREEN))
    screen.blit(fon, (0, 0))
    screen.blit(web, (0, 0))
    screen.blit(turn_bttn, (screenX / 2 - turn_bttn.get_width() / 2 - 8, 30))

    while True:

        if (not sleeping):

            if (clicked):

                if (turn < 50):

                    for i in range(50):

                        if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2:

                            if (turn < 49) and (player1[i] + player2[i] == 0):
                                if (memory >= 0):
                                    screen.blit(mass[memory], (web_list[memory][0] - mass[memory].get_width() / 2 - 3, web_list[memory][1] - mass[memory].get_height() / 2 - 2))
                                    screen.blit(players_gex[(turn + 1) % 2], (web_list[memory][0] - players_gex[(turn + 1) % 2].get_width() / 2, web_list[memory][1] - players_gex[(turn + 1) % 2].get_height() / 2))

                                screen.blit(mass[i], (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(circle, (web_list[i][0] - circle.get_width() / 2, web_list[i][1] - circle.get_height() / 2))
                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                memory = i

                                players[turn % 2][i] = 1
                                turn += 1
                                clicked = False

                            elif (turn == 49) and (player1[i] + player2[i] == 0):
                                screen.blit(mass[memory], (web_list[memory][0] - mass[memory].get_width() / 2, web_list[memory][1] - mass[memory].get_height() / 2))
                                screen.blit(players_gex[(turn + 1) % 2], (web_list[memory][0] - players_gex[(turn + 1) % 2].get_width() / 2, web_list[memory][1] - players_gex[(turn + 1) % 2].get_height() / 2))

                                players[turn % 2][i] = 1
                                turn += 1

                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                screen.blit(player2_gex, (web_list[i][0] - player2_gex.get_width() / 2, web_list[i][1] - player2_gex.get_height() / 2))

                                clicked = False

                        if i == 49:
                            clicked = False

                else:

                    if (not holding):

                        if (click_x >= screenX / 2 - turn_bttn.get_width() / 2 - 8) and (click_x <= screenX / 2 + turn_bttn.get_width() / 2 + 8) \
                            and (click_y >= 30) and (click_y <= 30 + turn_bttn.get_height()) :

                            if (turn % 2 == 1):
                                for i in range(2):
                                    if (players[turn % 2].count(1) - 24 > 0):
                                        pulls[i] += int(2 + abs(players[turn % 2].count(1) - 24) + turn - 50)

                                    else:
                                        pulls[i] += int(2 + round(0.1 * players[turn % 2].count(1)) + turn - 50)

                            for i in range(50):
                                av_move[i] = 0
                                av_attack[i] = 0

                            turn += 1
                            clicked = False

                        for i in range(50):

                            if ((web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2) and (players[turn % 2][i] == 1) and (pulls[turn % 2] > 0) :

                                pulls[turn % 2] -= am

                                if (pulls[turn % 2] < 0):
                                    am = am + pulls[turn % 2]
                                    pulls[turn % 2] = 0

                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                soldiers[i] += am

                                clicked = False

                                break

                        screen.blit(green_gex, (280 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("blue : " + str(pulls[0]), True, WHITE)
                        screen.blit(text, (screenX  / 8  - text.get_width() / 2 + 45, 10))

                        screen.blit(green_gex, (1624 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("red : " + str(pulls[1]), True, WHITE)
                        screen.blit(text, (screenX  / 8 * 7  - text.get_width() / 2 - 50, 10))

                        am = int(amount(screen, click_x, click_y, button_x1, button_x5, button_x10))
                        clicked = False

                    elif (time.time() - click_time > 1):

                        for i in range(50):

                            if ((web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2) and (players[turn % 2][i] == 1) and (soldiers[i] != 0) and ((av_move[i] == 0) or (av_attack[i] == 0)):
                                clicked = False
                                pointers = []

                                for j in range (50):
                                    if ((web_list[i][0] - web_list[j][0]) ** 2 + (web_list[i][1] - web_list[j][1]) ** 2 < 230 ** 2):

                                        if (players[(turn + 1) % 2][j] == 1) and (av_attack[i] != 1):
                                            pointers.append(j)

                                        elif (av_move[i] != 1) and (players[turn % 2][j] == 1):
                                            pointers.append(j)

                                for j in range(len(pointers)):
                                    if (pointers[j] != i):
                                        a = int((web_list[i][0] - web_list[pointers[j]][0]) / 168)
                                        b = int((web_list[i][1] - web_list[pointers[j]][1]) / 108)

                                        znak = anim[players[(turn+1) % 2][pointers[j]] == 1]

                                        screen.blit(arrows[a][b][players[(turn+1) % 2][pointers[j]] == 1], (web_list[i][0] + arrows[a][b][2], web_list[i][1] + arrows[a][b][3]))
                                        screen.blit(znak, (web_list[pointers[j]][0] - znak.get_width() / 2, web_list[pointers[j]][1] - znak.get_width() / 2))

                                pygame.display.flip()

                                while (clicked == False):

                                    for ev in pygame.event.get():

                                        if (ev.type == pygame.MOUSEBUTTONDOWN):
                                            clicked = True
                                            click_x, click_y = ev.pos

                                for j in range(len(pointers)):
                                    screen.blit(mass[pointers[j]], (web_list[pointers[j]][0] - mass[pointers[j]].get_width() / 2, web_list[pointers[j]][1] - mass[pointers[j]].get_height() / 2))

                                    if turn % 2 == 0:
                                        screen.blit(players_gex[players[(turn + 1) % 2][pointers[j]] == 1], ((web_list[pointers[j]][0] - player1_gex.get_width() / 2, web_list[pointers[j]][1] - player1_gex.get_height() / 2)))
                                    else:
                                        screen.blit(players_gex[players[turn % 2][pointers[j]] == 1], ((web_list[pointers[j]][0] - player1_gex.get_width() / 2, web_list[pointers[j]][1] - player1_gex.get_height() / 2)))

                                for j in range(50):

                                    if (web_list[j][0] - click_x) ** 2 + (web_list[j][1] - click_y) ** 2 < R ** 2:

                                        a = math.sqrt((web_list[i][0] - web_list[j][0]) ** 2 + (web_list[i][1] - web_list[j][1]) ** 2)

                                        if (a <= 230) and (web_list[j] != web_list[i]):

                                            if (players[turn % 2][j] == 1) and (av_move[i] == 0):

                                                soldiers[j] += soldiers[i]
                                                soldiers[i] = 0

                                                av_move[j] = 1

                                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))
                                                screen.blit(mass[i], (web_list[j][0] - mass[i].get_width() / 2, web_list[j][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[j][0] - players_gex[turn % 2].get_width() / 2, web_list[j][1] - players_gex[turn % 2].get_height() / 2))

                                            elif (players[(turn + 1) % 2][j] == 1) and (av_attack[i] == 0):

                                                s1 = int(round(soldiers[i] * random.uniform(0.4, 0.7)))
                                                s2 = 1 + int(round(soldiers[j] * random.uniform(0.7, 0.9)))

                                                av_attack[i] = 1

                                                soldiers[i] -= s2
                                                soldiers[j] -= s1

                                                screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))
                                                screen.blit(mass[i], (web_list[j][0] - mass[i].get_width() / 2, web_list[j][1] - mass[i].get_height() / 2))
                                                screen.blit(players_gex[(turn + 1) % 2], (web_list[j][0] - players_gex[(turn + 1) % 2].get_width() / 2, web_list[j][1] - players_gex[(turn + 1) % 2].get_height() / 2))

                                                if (soldiers[j] <= 0) and (soldiers[i] <= 0):

                                                    soldiers[i] = 0
                                                    soldiers[j] = 0

                                                elif (soldiers[j] <= 0):
                                                    players[(turn + 1) % 2][j] = 0
                                                    players[turn % 2][j] = 1

                                                    screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                                    screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))
                                                    screen.blit(mass[i], (web_list[j][0] - mass[i].get_width() / 2, web_list[j][1] - mass[i].get_height() / 2))
                                                    screen.blit(players_gex[turn % 2], (web_list[j][0] - players_gex[turn % 2].get_width() / 2, web_list[j][1] - players_gex[turn % 2].get_height() / 2))

                                                    av_attack[i] = 0
                                                    av_attack[j] = 1
                                                    av_move[i] = 0
                                                    av_move[j] = 1

                                                    soldiers[j] = soldiers[i]
                                                    soldiers[i] = 0

                                                elif (soldiers[i] <= 0):

                                                    av_attack[i] = 0
                                                    soldiers[i] = 0


                                        screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                                        screen.blit(players_gex[turn % 2], (web_list[i][0] - players_gex[turn % 2].get_width() / 2, web_list[i][1] - players_gex[turn % 2].get_height() / 2))

                                break

                        clicked = False

                for i in range(50):

                    if (soldiers[i] > 0 and soldiers[i] < 45):

                        for j in range(((soldiers[i] - soldiers[i] // 15 * 15) // 5) + 1):

                            screen.blit(heroes[soldiers[i] // 15], \
                            (web_list[i][0] - heroes[soldiers[i] // 15].get_width() / 2 - j * 10  , web_list[i][1] - heroes[soldiers[i] // 15].get_height() / 2 + j * 5))

                        text = fontCapture.render(str(soldiers[i]), True, (255, 255, 255, 255))
                        screen.blit(text, (web_list[i][0] - 15, web_list[i][1] - 70))

                if (turn % 2 == 0):
                    text = fontCapture.render("player 2", True, GREY)
                    screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                    text = fontCapture.render("player 1", True, WHITE)
                    screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

                else:
                    text = fontCapture.render("player 1", True, GREY)
                    screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                    text = fontCapture.render("player 2", True, WHITE)
                    screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

            pygame.display.flip()

        for ev in pygame.event.get():

            if (ev.type == pygame.QUIT):
                pygame.quit()
                break

            elif (ev.type == pygame.MOUSEBUTTONDOWN) and (clicked == False):
                click_time = time.time()
                clicked = True
                holding = True
                click_x, click_y = ev.pos

            elif (ev.type == pygame.MOUSEBUTTONUP):
                holding = False

def menu():
    screen.blit(zastavka, (0, 0))
    prev_time = time.time()
    counter = 0
    clicked = False

    while (True):

        if (clicked and click_x >= 1530 and click_x <= 1730\
                and click_y >= 70 and click_y <= 170):
            clicked = False
            playervsplayer()

        if (clicked and click_x >= 1530 and click_x <= 1730\
                and click_y >= 260 and click_y <= 360):

            clicked = False
            settings()

        if (clicked and click_x >= 1530 and click_x <= 1730\
                and click_y >= 750 and click_y <= 850):
            clicked = False
            pygame.quit()


        if (time.time() - prev_time >= 1):

            counter += 1
            screen.blit(grass[counter], (0, 806))
            screen.blit(jewslayer[counter], (0, 396))
            screen.blit(cloud1[counter], (420, 465))
            screen.blit(cloud2[counter], (720, 465))
            screen.blit(cloud3[counter], (1090, 465))
            screen.blit(cloud4[counter], (1870, 465))

            screen.blit(button_play, (1530, 70))
            screen.blit(button_exit, (1530, 750))
            screen.blit(button_settings, (1530, 260))

            pygame.display.flip()
            prev_time = time.time()

            if (counter % 6 == 0):
                counter = 0

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                click_x, click_y = ev.pos

def settings():
    global slider_x, song, game_start, web_list, player1, player2, mass, soldiers, turn, heroes, am, pulls

    textSound = fontDeja.render("Sound", True, BLACK)
    textPro = fontDeja.render("(" + str((slider_x - 620) // 31 * 5) + "%)", True, BLACK)
    clicked = False

    while(True):
        screen.blit(settings_list, (0,0))
        screen.blit(textSound, (750, 250))
        screen.blit(slider, (slider_x, 340))
        screen.blit(textPro, (1050, 250))

        pygame.display.flip()

        if (clicked == True):

            if (click_x <= 1138 and click_x >= 796) and (click_y <= 763  and click_y >= 655):
                game_start = False
                menu()

            if (click_x <= 360 or click_x >= 1560) or (click_y <= 210 or click_y >= 870):

                if game_start == False:
                    menu()
                else:
                    screen.fill((GREEN))
                    screen.blit(fon, (0, 0))
                    screen.blit(web, (0, 0))
                    screen.blit(turn_bttn, (screenX / 2 - turn_bttn.get_width() / 2 - 8, 30))
                    screen.blit(settings_game_button,(1920 / 2  + 328 - settings_game_button.get_width() / 2, settings_game_button.get_height()/2 ))

                    for i in range(50):
                        if player1[i]==1:
                            screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                            screen.blit(player1_gex, (web_list[i][0] - player1_gex.get_width() / 2, web_list[i][1] - player1_gex.get_height() / 2))
                        if player2[i]==1:
                            screen.blit(mass[i], (web_list[i][0] - mass[i].get_width() / 2, web_list[i][1] - mass[i].get_height() / 2))
                            screen.blit(player2_gex, (web_list[i][0] - player2_gex.get_width() / 2, web_list[i][1] - player2_gex.get_height() / 2))

                    for i in range(50):

                        if (soldiers[i] > 0 and soldiers[i] < 45):

                            for j in range(((soldiers[i] - soldiers[i] // 15 * 15) // 5) + 1):

                                screen.blit(heroes[soldiers[i] // 15], \
                                (web_list[i][0] - heroes[soldiers[i] // 15].get_width() / 2 - j * 10  , web_list[i][1] - heroes[soldiers[i] // 15].get_height() / 2 + j * 5))

                            text = fontCapture.render(str(soldiers[i]), True, (255, 255, 255, 255))
                            screen.blit(text, (web_list[i][0] - 15, web_list[i][1] - 70))

                    if turn>=50:
                        if (turn % 2 == 0):
                            text = fontCapture.render("player 2", True, GREY)
                            screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                            text = fontCapture.render("player 1", True, WHITE)
                            screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

                        else:
                            text = fontCapture.render("player 1", True, GREY)
                            screen.blit(text, (screenX  / 2 - text.get_width() / 2, 0))
                            text = fontCapture.render("player 2", True, WHITE)
                            screen.blit(text, (screenX  / 2  - text.get_width() / 2, 0))

                        screen.blit(green_gex, (280 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("blue : " + str(pulls[0]), True, WHITE)
                        screen.blit(text, (screenX  / 8  - text.get_width() / 2 + 45, 10))

                        screen.blit(green_gex, (1624 - green_gex.get_width() / 2, -108))
                        text = fontCapture.render("red : " + str(pulls[1]), True, WHITE)
                        screen.blit(text, (screenX  / 8 * 7  - text.get_width() / 2 - 50, 10))

                        am = int(amount(screen, click_x, click_y, button_x1, button_x5, button_x10))
                    break



            elif (clicked and click_x >= 620 and click_x <= 1240\
                    and click_y >= 310 and click_y <= 536):

                while (clicked == True):

                    if (slider_x > 1240):
                        slider_x = 1240

                    elif (slider_x < 620):
                        slider_x = 620

                    slider_x = (slider_x - 620) // 31 * 31 + 620

                    song.set_volume((slider_x - 620) // 31 / (20 * 1.0))

                    textPro = fontDeja.render("(" + str((slider_x - 620) // 31 * 5) + "%)", True, BLACK)
                    screen.blit(settings_list, (0,0))
                    screen.blit(textSound, (750, 250))
                    screen.blit(textPro, (1050, 250))
                    screen.blit(slider, (slider_x, 340))
                    pygame.display.flip()

                    for ev in pygame.event.get():

                        if ev.type == pygame.MOUSEBUTTONUP:
                            clicked = False

                        elif ev.type == pygame.MOUSEMOTION:
                            slider_x = ev.pos[0]




            clicked = False

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                click_x, click_y = ev.pos


menu()


#python android.py --launch build /home/egor/ProjectA release install
