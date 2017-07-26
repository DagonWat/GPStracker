import pygame, os
def amount(screen, clicked_x, clicked_y, button1, button2,  button3):
    amount = 1
    screen.blit(button1,(1920 / 2 - 342 - button1.get_width() / 2, 1080 - 1.5 * button1.get_height()))
    screen.blit(button2,(1920 / 2 - button2.get_width() / 2 - 8, 1080 - 1.5 * button2.get_height()))
    screen.blit(button3,(1920 / 2  + 328 - button3.get_width() / 2, 1080 - 1.5 * button3.get_height()))


    if clicked_x < (1920 / 2 - 342  + button1.get_width() / 2) and clicked_x > (1920 / 2 - 342 - button1.get_width() / 2) and clicked_y > 1080 - 1.5 * button1.get_height():
        amount = 1
    if clicked_x < (1920 / 2 + button2.get_width() / 2) and clicked_x > (1920 / 2 - button2.get_width() / 2) and clicked_y > 1080 - 1.5 * button2.get_height():
        amount = 5
    if clicked_x < (1920 / 2  + 328 + button3.get_width() / 2) and clicked_x > (1920 / 2  + 328 - button3.get_width() / 2) and clicked_y > 1080 - 1.5 * button3.get_height():
        amount = 10

    return amount
