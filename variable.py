import pygame
import random
import os

pygame.mixer.init()

#Game Screen
screenWidth = 800
screenHeight = 600
fps = 60
flags = 0 #pygame.FULLSCREEN|pygame.HWSURFACE
game_folder = os.path.dirname(__file__)   
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((screenWidth, screenHeight), flags)

#Color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
violet = (255,0,255)
skyblue = (0,255,255)

color_head = (red,green,blue,yellow)

#Snake Var


blocksize = 25

up = 0
right = 1
down = 2
left = 3
downleft = 4
downright = 5
upleft = 6
upright = 7

music_folder = os.path.join(game_folder, 'music') 

beep_array = {
    'beep01' : pygame.mixer.Sound(os.path.join(music_folder, "Blip_Select12.wav")) ,#Hit
    'beep04' : pygame.mixer.Sound(os.path.join(music_folder, "Powerup6.wav")) ,#Hit
    'beep03' : pygame.mixer.Sound(os.path.join(music_folder, "Powerup.wav")) ,#Hit
    'beep02' : pygame.mixer.Sound(os.path.join(music_folder, "Powerup11.wav")) ,#Hit
    }

font_array = {
    'african' : os.path.join(game_folder, "african.ttf"),
    'wood_sticks': os.path.join(game_folder, "wood_sticks.ttf"),
    }

font_typo = {0: (font_array['african'],50), 
             1:(font_array['african'],30),
}
font_color = {0: (black, white),
              1: (white, None),
              2: ((50,50,50),None),
              3: (black, None),
              4: ((0,175,0), None),
              5: ((1,1,1),None),
              6: ((0,100,0),None),
}


def textdisplay(message, color, fontset):
    font = pygame.font.Font(fontset[0],fontset[1])
    text = font.render(message, True, color[0], color[1])
    textRect = text.get_rect()
    
    return text,textRect