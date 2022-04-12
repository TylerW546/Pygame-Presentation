# Program--Create a Jackson Pollock 

# Import some libraries
import pygame
import random
import time
import math
import os
from pygame.locals import *  #don't need on home computer
 
# Initialize the game engine
pygame.init()
 
# Define some basic colors in RGB format. You can create your own colors if you want more options.
BLACK = (  0,   0,   0)
GRAY =  (150, 150, 150)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
CYAN =  (  0, 255, 255)
MAGENTA = (255,  0, 255)

def customDisplayUpdate():
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
    pygame.display.update()

# function to draw a grid with guidelines
def drawGridLines(screen):
   for i in range(screen.get_rect().width // 10):
      pygame.draw.line(screen, (200,200,200), [0 + i*10, 0], [0 + i*10,screen.get_rect().height], 1)
      pygame.draw.line(screen, (200,200,200), [0, 0 + i*10], [screen.get_rect().width,0 + i*10], 1)
   for i in range(screen.get_rect().width // 10):
      pygame.draw.line(screen, (100,100,100), [0 + i*100, 0], [0 + i*100,screen.get_rect().height], 1)
      pygame.draw.line(screen, (100,100,100), [0, 0 + i*100], [screen.get_rect().width,0 + i*100], 1)
      
# function to convert angle degrees to radians
def toRadians(degrees):
   return degrees * math.pi / 180 
 
def drawToScreen(screen):
   # Clear the screen and set the screen background
   screen.fill(WHITE)
    
   # use this function to draw grid lines on screen
   drawGridLines(screen)
   
 
   #1. DRAWING RANDOM LINES
   for i in range(1000):
      x1 = random.randint(0,1000)
      y1 = random.randint(0,800)
      x2 = random.randint(0,1000)
      y2 = random.randint(0,800)
      
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      RANDOMCOLOR = (red, green, blue)
      
      lineSize = random.randint(1,40)
   
      pygame.draw.line(screen, RANDOMCOLOR, [x1, y1], [x2, y2], lineSize)
      time.sleep(.001)
      customDisplayUpdate()
   
   time.sleep(1)
   screen.fill(WHITE)
   
   
   #2. DRAW RANDOM SQUARES
   for i in range(1000):
      x1 = random.randint(-50,1000)
      y1 = random.randint(-50,800)
      width = random.randint(5,200)
      height = random.randint(5,200)
      
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      RANDOMCOLOR = (red, green, blue)
      
      lineSize = random.randint(0,30)
   
      pygame.draw.rect(screen, RANDOMCOLOR, [x1, y1, width, height], lineSize)
      customDisplayUpdate()
   
   time.sleep(1)
   screen.fill(WHITE)
   
   
   #3. DRAW RANDOM ELLIPSES
   for i in range(1000):
      x1 = random.randint(-50,1000)
      y1 = random.randint(-50,800)
      width = random.randint(10,200)
      height = random.randint(10,200)
      
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      RANDOMCOLOR = (red, green, blue)
      
      lineSize = random.randint(0,5) #can't be greater than ellipse radius
   
      pygame.draw.ellipse(screen, RANDOMCOLOR, [x1, y1, width, height], lineSize)
      customDisplayUpdate()
         
   time.sleep(1) # the parameter is in seconds
   screen.fill(WHITE)
   
   
   #4. DRAW RANDOM ARCS (SQUIGGLES)
   for i in range(1000):
      x1 = random.randint(-50,1000)
      y1 = random.randint(-50,800)
      width = random.randint(10,200)
      height = random.randint(10,200)
      
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      RANDOMCOLOR = (red, green, blue)
      
      startAngle = random.randint(0,359)
      endAngle = random.randint(0,359)
      
      lineSize = random.randint(0,5) #can't be greater than ellipse radius
   
      pygame.draw.arc(screen, RANDOMCOLOR,[x1, y1, width, height], toRadians(startAngle), toRadians(endAngle), lineSize)
      customDisplayUpdate()
         
   time.sleep(1) # the parameter is in seconds
   screen.fill(WHITE)
   
   #5. DRAW RANDOM POLYGONS
   for i in range(500):
      x1 = random.randint(-50,1000)
      y1 = random.randint(-50,800)
      x2 = random.randint(-50,1000)
      y2 = random.randint(-50,800)
      x3 = random.randint(-50,1000)
      y3 = random.randint(-50,800)
      x4 = random.randint(-50,1000)
      y4 = random.randint(-50,800)
      
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      RANDOMCOLOR = (red, green, blue)
      
      lineSize = random.randint(1,10) #can't be greater than ellipse radius
   
      pygame.draw.polygon(screen, RANDOMCOLOR, [ [x1, y1], [x2, y2], [x3, y3], [x4, y4] ], 0) 
      customDisplayUpdate()
         
   time.sleep(1) # the parameter is in seconds
   screen.fill(WHITE)
   
   #6. CREATE YOUR OWN MASTERPIECE
   
   #top left
   for i in range(500):
      x1 = random.randint(0,screen.get_rect().width/2 + 20)
      y1 = random.randint(0,screen.get_rect().height/2 + 20)
      x2 = random.randint(0,screen.get_rect().width/2 + 20)
      y2 = random.randint(0,screen.get_rect().height/2 + 20)
      
      #create a random color
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,255)
      RANDOMCOLOR =  (red, green, blue)
      
      lineSize = random.randint(1,25)
      
      pygame.draw.line(screen, RANDOMCOLOR, [x1, y1], [x2,y2], lineSize)
      time.sleep(0.001)
      customDisplayUpdate()
      
   #top right
   for i in range(500):
      x1 = random.randint(screen.get_rect().width/2-20,screen.get_rect().width)
      y1 = random.randint(0,screen.get_rect().height/2-20)
      width = random.randint(10,100)
      height = random.randint(10,100)
      
      #create a random color
      red = random.randint(0,255)
      green = random.randint(0,255)
      blue = random.randint(0,0)
      RANDOMCOLOR =  (red, green, blue)
      
      lineSize = random.randint(0,25)
      
      pygame.draw.rect(screen, RANDOMCOLOR, [x1, y1, width, height], lineSize)
      time.sleep(0.001)
      customDisplayUpdate()
   
   #bottom left
   for i in range(1000):
      x1 = random.randint(-100,screen.get_rect().width/2)
      y1 = random.randint(screen.get_rect().height/2-20,screen.get_rect().height)
      width = random.randint(30,50)
      height = random.randint(20,40)
      
      #create a random color
      red = random.randint(0,255)
      green = random.randint(0,0)
      blue = random.randint(0,0)
      RANDOMCOLOR =  (red, green, blue)
      
      lineSize = random.randint(1,10)
      
      pygame.draw.ellipse(screen, RANDOMCOLOR, [x1, y1, width, height], lineSize)
      time.sleep(0.001)
      customDisplayUpdate()
   
   #bottom right
   for i in range(500):
      x1 = random.randint(screen.get_rect().width/2,screen.get_rect().width)
      y1 = random.randint(screen.get_rect().height/2,screen.get_rect().height)
      x2 = random.randint(screen.get_rect().width/2,screen.get_rect().width)
      y2 = random.randint(screen.get_rect().height/2,screen.get_rect().height)
      x3 = random.randint(screen.get_rect().width/2,screen.get_rect().width)
      y3 = random.randint(screen.get_rect().height/2,screen.get_rect().height)
      x4 = random.randint(screen.get_rect().width/2,screen.get_rect().width)
      y4 = random.randint(screen.get_rect().height/2,screen.get_rect().height)
      x5 = random.randint(screen.get_rect().width/2,screen.get_rect().width)
      y5 = random.randint(screen.get_rect().height/2,screen.get_rect().height)
      
      #create a random color
      red = random.randint(200,255)
      green = random.randint(200,255)
      blue = random.randint(200,255)
      RANDOMCOLOR =  (red, green, blue)
      
      lineSize = random.randint(0,10)
      
      pygame.draw.polygon(screen, RANDOMCOLOR, [ [x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5] ], 0)

      time.sleep(0.001)
      customDisplayUpdate()
   
   #frame
   pygame.draw.line(screen, BLACK, [0, screen.get_rect().height/2], [screen.get_rect().width,screen.get_rect().height/2], 20)
   pygame.draw.line(screen, BLACK, [screen.get_rect().width/2, 0], [screen.get_rect().width/2,screen.get_rect().height], 20)
   
   #middle drawing
   for i in range(900):
      x1 = random.randint(screen.get_rect().width/2+100,screen.get_rect().width-100)
      y1 = random.randint(screen.get_rect().height/2+100,screen.get_rect().height-100)
      width = random.randint(30,50)
      height = random.randint(20,40)
      
      #create a random color
      red = random.randint(0,200)
      green = random.randint(0,200)
      blue = random.randint(0,200)
      RANDOMCOLOR =  (red, green, blue)
      
      randomAngle1 = random.randint(0,359)
      randomAngle2 = random.randint(0,359)
      
      lineSize = random.randint(1,10)
      
      pygame.draw.arc(screen, RANDOMCOLOR,[x1, y1, width, height], toRadians(randomAngle1), toRadians(randomAngle2), 1)
      
      time.sleep(0.001)
      customDisplayUpdate()
   
   # ALL DRAWING CODE HAPPENS ABOVE THIS COMMENT: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

   # Update the display after all of the all the other drawing commands.
   customDisplayUpdate()
   time.sleep(2) #slows down while loop, if necessary
   return 1

