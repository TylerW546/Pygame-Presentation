import math
import pygame
from pygame.locals import *
import random
import time

from program0 import drawToScreen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCALE = 1

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE,SCREEN_HEIGHT * SCALE))

numFiles = 3

drawFunctions = []
for i in range(numFiles): 
    with open("program" + str(i) + ".py") as f:
        exec(compile(f.read(), "program" + str(i) + ".py", "exec"))
    drawFunctions.append(drawToScreen)

def main():
    # Every 100 is a second
    timerMax = 300
    timer = 0
    programNumber = -1
    while (True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        if timer == 0:
            programNumber += 1
            programNumber %= numFiles

        screen.fill(black)

        drawFunctions[programNumber](screen)

        pygame.display.update()
        

        timer = (timer + 1) % timerMax
        time.sleep(.01)

if __name__ == "__main__":
    main()