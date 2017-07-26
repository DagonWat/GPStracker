import pygame, os
def amount(clicked, clicked_x, cliked_y, button, button_width, button_height):
    amount = 1
    pygame.display.blit(button1,(1920 / 2 - button1_width / 2, 0))
    if cliked_x < (1920 / 2 + button_width / 2) and cliked_x > (1920 / 2 - button_width / 2) and cliked_y < button_height and cliked_x > 0:
        if clicked_y < button_height / 3:
            amount = 1
        elif clicked_y > button_height / 3 and clicked_y < button_height * 2 / 3 :
            amount = 5
        else:
            amount = 10
    return amount
