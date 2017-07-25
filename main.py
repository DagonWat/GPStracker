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

    memory = [10000, 10000]

    player1 = []
    player2 = []
    soldiers = []

    for i in range(50):
        soldiers.append(0)
        player1.append(0)
        player2.append(0)


    turn = 0


    screen.fill((GREEN))
    screen.blit(web, (0, 0))

    while True:

        if not sleeping:

            if clicked:

                if turn < 50:

                    for i in range(0, 50):

                        if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2:

                            if turn % 2 == 0 and player2[i] == 0 and player1[i] == 0:

                                screen.blit(green_gex, (memory[0] - green_gex.get_width() / 2, memory[1] - green_gex.get_height() / 2))
                                screen.blit(player2_gex, (memory[0] - player2_gex.get_width() / 2, memory[1] - player2_gex.get_height() / 2))

                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(circle, (web_list[i][0] - circle.get_width() / 2, web_list[i][1] - circle.get_height() / 2))
                                screen.blit(player1_gex, (web_list[i][0] - player1_gex.get_width() / 2, web_list[i][1] - player1_gex.get_height() / 2))

                                memory = [web_list[i][0], web_list[i][1]]

                                turn += 1
                                player1[i] = 1
                                clicked = False

                            elif turn % 2 == 1 and player1[i] == 0 and player2[i] == 0:


                                screen.blit(green_gex, (memory[0] - green_gex.get_width() / 2, memory[1] - green_gex.get_height() / 2))
                                screen.blit(player1_gex, (memory[0] - player1_gex.get_width() / 2, memory[1] - player1_gex.get_height() / 2))

                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(circle, (web_list[i][0] - circle.get_width() / 2, web_list[i][1] - circle.get_height() / 2))
                                screen.blit(player2_gex, (web_list[i][0] - player2_gex.get_width() / 2, web_list[i][1] - player2_gex.get_height() / 2))

                                memory = [web_list[i][0], web_list[i][1]]

                                turn += 1
                                player2[i] = 1
                                clicked = False

                            if turn == 50:
                                screen.blit(green_gex, (memory[0] - green_gex.get_width() / 2, memory[1] - green_gex.get_height() / 2))
                                screen.blit(player1_gex, (memory[0] - player1_gex.get_width() / 2, memory[1] - player1_gex.get_height() / 2))

                            if i == 49:
                                clicked = False

                else:
                    for i in range(50):

                        if (web_list[i][0] - click_x) ** 2 + (web_list[i][1] - click_y) ** 2 < R ** 2:

                            soldiers[i] += 1
                            turn += 1
                            clicked = False

                            if player1[i] == 1:
                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(player1_gex, (web_list[i][0] - player1_gex.get_width() / 2, web_list[i][1] - player1_gex.get_height() / 2))

                            elif player2[i] == 1:
                                screen.blit(green_gex, (web_list[i][0] - green_gex.get_width() / 2, web_list[i][1] - green_gex.get_height() / 2))
                                screen.blit(player2_gex, (web_list[i][0] - player2_gex.get_width() / 2, web_list[i][1] - player2_gex.get_height() / 2))

            for i in range(50):

                if soldiers[i] != 0 and soldiers[i] < 10:
                    screen.blit(soldier, (web_list[i][0] - soldier.get_width() / 2, web_list[i][1] - soldier.get_height() / 2))

                    if soldiers[i] == 2:
                        screen.blit(soldier, (web_list[i][0] - soldier.get_width() / 2 - 10 , web_list[i][1] - soldier.get_height() / 2))
                    if soldiers[i] >= 3:
                        screen.blit(soldier, (web_list[i][0] - soldier.get_width() / 2 - 10 , web_list[i][1] - soldier.get_height() / 2))
                        screen.blit(soldier, (web_list[i][0] - soldier.get_width() / 2 - 20 , web_list[i][1] - soldier.get_height() / 2))

                    text = fontCapture.render(str(soldiers[i]), True, (255, 255, 255, 255))
                    screen.blit(text, (web_list[i][0] -15, web_list[i][1]- 70))

                elif soldiers[i] >= 10 and soldiers[i] < 30:
                    screen.blit(hourse, (web_list[i][0] - hourse.get_width() / 2, web_list[i][1] - hourse.get_height() / 2))

                    if soldiers[i] >= 15 and soldiers[i] <= 20 :
                        screen.blit(hourse, (web_list[i][0] - hourse.get_width() / 2 - 10 , web_list[i][1] - hourse.get_height() / 2))

                    if soldiers[i] > 20 and soldiers[i] < 30 :
                        screen.blit(hourse, (web_list[i][0] - hourse.get_width() / 2 - 10 , web_list[i][1] - hourse.get_height() / 2))
                        screen.blit(hourse, (web_list[i][0] - hourse.get_width() / 2 - 20 , web_list[i][1] - hourse.get_height() / 2))

                    text = fontCapture.render(str(soldiers[i]), True, (255, 255, 255, 255))
                    screen.blit(text, (web_list[i][0] -15, web_list[i][1]- 70))

                elif soldiers[i] >= 30:
                    screen.blit(tevton, (web_list[i][0] - tevton.get_width() / 2, web_list[i][1] - tevton.get_height() / 2))

                    if soldiers[i] >= 40 and soldiers[i] <= 50 :
                        screen.blit(tevton, (web_list[i][0] - tevton.get_width() / 2 - 10 , web_list[i][1] - tevton.get_height() / 2))

                    if soldiers[i] > 50:
                        screen.blit(tevton, (web_list[i][0] - tevton.get_width() / 2 - 10 , web_list[i][1] - tevton.get_height() / 2))
                        screen.blit(tevton, (web_list[i][0] - tevton.get_width() / 2 - 20 , web_list[i][1] - tevton.get_height() / 2))

                    text = fontCapture.render(str(soldiers[i]), True, (255, 255, 255, 255))
                    screen.blit(text, (web_list[i][0] -15, web_list[i][1]- 70))

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
