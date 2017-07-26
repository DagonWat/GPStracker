import pygame, os
def amount(clicked_x, clicked_y, button1, button2,  button3,):
    amount = 1
    pygame.display.blit(button1,(1920 / 4 - button1.get_width() / 2, 1080 - button1.get_height()))
    pygame.display.blit(button1,(1920 / 2 - button2.get_width() / 2, 1080 - button2.get_height()))
    pygame.display.blit(button1,(1920 / 4 * 3 - button3.get_width() / 2, 1080 - button3.get_height()))


    if clicked_x < (1920 / 4 + button1.get_width() / 2) and clicked_x > (1920 / 4 - button1.get_width() / 2) and clicked_y > 1080 - button1.get_height():
        amount = 1
    if clicked_x < (1920 / 2 + button2.get_width() / 2) and clicked_x > (1920 / 2 - button2.get_width() / 2) and clicked_y > 1080 - button2.get_height():
        amount = 5
    if clicked_x < (1920 / 4 * 3 + button3.get_width() / 2) and clicked_x > (1920 / 4 * 3 - button3.get_width() / 2) and clicked_y > 1080 - button3.get_height():
        amount = 10

    return amount
