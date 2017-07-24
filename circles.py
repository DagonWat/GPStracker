#import pygame_sdl2
#pygame_sdl2.import_as_pygame()

import pygame

web_list = []

for i in range(0, 11):

    if i % 2 == 0:
        for j in range(0, 5):
            web_list.append((112 + 168 * i, 108 + 216 * j))

    else:
        for j in range(0, 4):
            web_list.append((112 + 168 * i, 216 + 216 * j))

R = 113
