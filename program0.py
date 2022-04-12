# DRAWING RANDOM IMAGES

import math
import pygame
from pygame.locals import *
import random
import time

timePerImage = 100
images = 14
timer = 0
imageNumber = 0

def drawToScreen(screen):
    global imageNumber
    global timer
    global images
    global timePerImage
    
    image = pygame.image.load('images/image' + str(imageNumber) + '.png')
    height = 0
    width = 0
    if image.get_rect().width / image.get_rect().height > screen.get_rect().width/screen.get_rect().height:
        width = screen.get_rect().width
        height = round(width * image.get_rect().height/image.get_rect().width)
    else:
        height = screen.get_rect().height
        width = round(height * image.get_rect().width/image.get_rect().height)
        
    image = pygame.transform.scale(image, (width,height)) 
    blitLocation = image.get_rect(center=(screen.get_rect().width/2, screen.get_rect().height/2))
    screen.blit(image, blitLocation)
    
    timer = (timer + 1) % timePerImage
    if timer == 0:
        imageNumber = (imageNumber + 1) % images
    return timePerImage * images
