import math
import pygame
from pygame.locals import *
import random
import time

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

squareWidth = 100

def drawToScreen(screen):
    # Fill Green Circles
    for i in range(4):
        for j in range(3):
            pygame.draw.circle(screen, green, (i*2*squareWidth+j%2*squareWidth+squareWidth//2,j*squareWidth+squareWidth//2),squareWidth//3, 0)
