import math
import pygame
from pygame.locals import *
import random
import time

from main import SCREEN_WIDTH_REAL
from main import SCREEN_HEIGHT_REAL
SCREEN_WIDTH = 100
SCREEN_HEIGHT = round(100*SCREEN_HEIGHT_REAL/SCREEN_WIDTH_REAL)
SCALE = SCREEN_WIDTH_REAL//SCREEN_WIDTH

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
blue = (0, 0, 255)

def drawToScreen(screen):
    SCALE = 3
    from Slime import Slime
    from DataMap import DataMap

    slimePercent = .07
    slimeCount = int(SCREEN_WIDTH*SCREEN_HEIGHT*slimePercent)

    for i in range(slimeCount):
        Slime.add(Slime(x=random.randrange(5,SCREEN_WIDTH-5), y=random.randrange(5,SCREEN_HEIGHT-5), angle=random.randrange(0,360)))

    
    pause = False
    viewDataMap = True
    for loop in range(500):
        decay = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not(pause)
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    viewDataMap = not viewDataMap
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            decay = True
        
        screen.fill(black)

        if not pause:
            DataMap.diffuse()
            DataMap.decay()
            Slime.updateAll()
            
        if decay and viewDataMap:
            DataMap.diffuse()
            DataMap.decay()
        
        if viewDataMap:
            DataMap.draw(screen)
        else:
            Slime.drawAllscreen()

        pygame.display.update()
        
        time.sleep(.001)
    return 1