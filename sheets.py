#import pygame_sdl2
#pygame_sdl2.import_as_pygame()

import pygame, os

web = pygame.image.load(os.path.join("pics", "web_fullHD.png"))
circle = pygame.image.load(os.path.join("pics", "circle.png"))
player1_gex = pygame.image.load(os.path.join("pics", "player1_gex.png"))
player2_gex = pygame.image.load(os.path.join("pics", "player2_gex.png"))
soldier = pygame.image.load(os.path.join("pics", "soldier.png"))
horse = pygame.image.load(os.path.join("pics", "horse.png"))
green_gex = pygame.image.load(os.path.join("pics", "green_gex.png"))
tevton = pygame.image.load(os.path.join("pics", "tevton.png"))
turn_bttn = pygame.image.load(os.path.join("pics", "button.png"))
button_x1 = pygame.image.load(os.path.join("pics", "button1.png"))
button_x5 = pygame.image.load(os.path.join("pics", "button2.png"))
button_x10 = pygame.image.load(os.path.join("pics", "button3.png"))
green_down = pygame.image.load(os.path.join("pics", "green_down.png"))
green_down_left = pygame.image.load(os.path.join("pics", "green_down_left.png"))
green_down_right = pygame.image.load(os.path.join("pics", "green_down_right.png"))
green_up = pygame.image.load(os.path.join("pics", "green_up.png"))
green_up_left = pygame.image.load(os.path.join("pics", "green_up_left.png"))
green_up_right = pygame.image.load(os.path.join("pics", "green_up_right.png"))
red_down = pygame.image.load(os.path.join("pics", "red_down.png"))
red_down_left = pygame.image.load(os.path.join("pics", "red_down_left.png"))
red_down_right = pygame.image.load(os.path.join("pics", "red_down_right.png"))
red_up = pygame.image.load(os.path.join("pics", "red_up.png"))
red_up_left = pygame.image.load(os.path.join("pics", "red_up_left.png"))
red_up_right = pygame.image.load(os.path.join("pics", "red_up_right.png"))
zastavka = pygame.image.load(os.path.join("pics/menu", "zastavka2.png"))
plus = pygame.image.load(os.path.join("pics", "plusik.png"))
sword = pygame.image.load(os.path.join("pics", "sword.png"))

cloud1_1 = pygame.image.load(os.path.join("pics/menu", "cloud1_1.png"))
cloud1_2 = pygame.image.load(os.path.join("pics/menu", "cloud1_2.png"))
cloud1_3 = pygame.image.load(os.path.join("pics/menu", "cloud1_3.png"))
cloud1_4 = pygame.image.load(os.path.join("pics/menu", "cloud1_4.png"))
cloud1_5 = pygame.image.load(os.path.join("pics/menu", "cloud1_5.png"))
cloud1_6 = pygame.image.load(os.path.join("pics/menu", "cloud1_6.png"))
cloud2_1 = pygame.image.load(os.path.join("pics/menu", "cloud2_1.png"))
cloud2_2 = pygame.image.load(os.path.join("pics/menu", "cloud2_2.png"))
cloud2_3 = pygame.image.load(os.path.join("pics/menu", "cloud2_3.png"))
cloud2_4 = pygame.image.load(os.path.join("pics/menu", "cloud2_4.png"))
cloud2_5 = pygame.image.load(os.path.join("pics/menu", "cloud2_5.png"))
cloud2_6 = pygame.image.load(os.path.join("pics/menu", "cloud2_6.png"))
cloud3_1 = pygame.image.load(os.path.join("pics/menu", "cloud3_1.png"))
cloud3_2 = pygame.image.load(os.path.join("pics/menu", "cloud3_2.png"))
cloud3_3 = pygame.image.load(os.path.join("pics/menu", "cloud3_3.png"))
cloud3_4 = pygame.image.load(os.path.join("pics/menu", "cloud3_4.png"))
cloud3_5 = pygame.image.load(os.path.join("pics/menu", "cloud3_5.png"))
cloud3_6 = pygame.image.load(os.path.join("pics/menu", "cloud3_6.png"))
cloud4_1 = pygame.image.load(os.path.join("pics/menu", "cloud4_1.png"))
cloud4_2 = pygame.image.load(os.path.join("pics/menu", "cloud4_2.png"))
cloud4_3 = pygame.image.load(os.path.join("pics/menu", "cloud4_3.png"))
cloud4_4 = pygame.image.load(os.path.join("pics/menu", "cloud4_4.png"))
cloud4_5 = pygame.image.load(os.path.join("pics/menu", "cloud4_5.png"))
cloud4_6 = pygame.image.load(os.path.join("pics/menu", "cloud4_6.png"))

settings_list = pygame.image.load(os.path.join("pics/menu", "settings_list.png"))
slider = pygame.image.load(os.path.join("pics/menu", "slider.png"))


jewslayer1 = pygame.image.load(os.path.join("pics/menu", "jewslayer1.png"))
jewslayer2 = pygame.image.load(os.path.join("pics/menu", "jewslayer2.png"))
jewslayer3 = pygame.image.load(os.path.join("pics/menu", "jewslayer3.png"))

grass1 = pygame.image.load(os.path.join("pics/menu", "grass_left.png"))
grass2 = pygame.image.load(os.path.join("pics/menu", "grass_normal.png"))
grass3 = pygame.image.load(os.path.join("pics/menu", "grass_right.png"))
grass4 = pygame.image.load(os.path.join("pics/menu", "grass_right_max.png"))


button_exit = pygame.image.load(os.path.join("pics/menu", "button_exit.png"))
button_play = pygame.image.load(os.path.join("pics/menu", "button_play.png"))
button_settings = pygame.image.load(os.path.join("pics/menu", "button_settings.png"))


fon = pygame.image.load(os.path.join("pics", "fon.png"))
mass = []
for i in range(1,51):
    mass.append(0)
    k = str(i) + ".png"
    background = pygame.image.load(os.path.join("pics/background", k))
    mass[i-1] = background
