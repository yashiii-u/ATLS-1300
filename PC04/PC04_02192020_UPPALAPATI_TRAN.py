#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# PC04 Interactive Robot

#

# UPPALAPATI, TRAN

#

# 02/19/2020

# Description - A robot is drawn and chasing a ball around using the arrow keys, 
getting angry when it doesn't reach it and increasing it's size when hitting the 
enter key

@author: Michelle
# -*- coding: utf-8 -*-
"""

#PSEUDOCODE
#PSEUDOCODE
#create robot - rectangle head, circles for eyes, trapezoid body with circles for buttons, 
#and white circles for wheels, drew a circle to create the ball
#using arrow keys will move the robot, hitting enter
#will cause it to go "angry" by increasing in size. 


import pygame
from random import *

#set up colors
BLACK = (0,0,0)
RED = (255,0,0)
PINK = (170,0,50)
GREEN = (0,255,0)
BLUE = (0,0,255)
LT_BLUE = (0, 100, 255)
WHITE = (255,255,255)
GRAY = (127,127,127)
DK_GRAY = (100,100,100)

#create screen and game variables
size = 500
screen =  pygame.display.set_mode((size,size)) #create 500 x500 pixel screen

run = True
x = size/2 #center position for all robot parts
y = size/2
scale = 1 #variable to adjust when keys are pressed to change size of robot
speed = 2
eye_r = 2
rSize = 5



#Robo features
blink = [GREEN, BLUE, RED, LT_BLUE]
color = choice(blink) #assign a value to color
colorL = choice(blink) #assign a value to color
colorR = choice(blink) #assign a value to color

#Game loop
while run:
    # create exit-on click detection:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
            
    #Drawing goes from bottom to top. We'll make our screen white first, then
    #add the robo-parts.    
    screen.fill(BLACK)
                #sets the arrow keys to the rotbot 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
            y += speed
    
    if keys[pygame.K_RETURN]:
        if rSize <=5:
            rSize +=5
        elif rSize >5:
            rSize -=5

#Code gotten from CANVAS website - altered minimally
    #Pygame draw docs: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    Head = pygame.draw.rect(screen,WHITE,(x-25,y-90,50,75),rSize) #draing the head
    Body = pygame.draw.polygon(screen, WHITE, [(x+35, y-35),(x+45,y+35), (x-45,y+35),(x-35, y-35)]) #drawing the body
    L_eye = pygame.draw.circle(screen, GREEN, (int(x-10), int(y-70)),rSize) #drawing th eleft eye
    R_eye = pygame.draw.circle(screen, GREEN, (int(x+10), int(y-70)),rSize) #drawing the right eye
    panelLights1 = pygame.draw.circle(screen, colorR, (int(x+20), int(y-5)),rSize) #drawing the lights
    panelLights2 = pygame.draw.circle(screen, color, (int(x), int(y-5)),rSize)  #drawing the lights
    panelLights3 = pygame.draw.circle(screen, colorL, (int(x-20), int(y-5)),rSize)  #drawing the lights

    L_wheel = pygame.draw.circle(screen, BLACK, (int(x-40), int(y+63)),20)  #drawing the left wheel
    R_wheel = pygame.draw.circle(screen, BLACK, (int(x+40), int(y+63)),20)  #drawing the right wheel 
    L_hub = pygame.draw.circle(screen, WHITE, (int(x-40), int(y+63)),10)  #drawing the left hub
    R_hub = pygame.draw.circle(screen, WHITE, (int(x+40), int(y+63)),10)  #drawing the right hub
    Track = pygame.draw.ellipse(screen, WHITE, (int(x-65), int(y+33),130,60),rSize)  #drawing the trakc
    

# We tried a lot of different types of code and a lot of them wouldn't work for some reason
#while run:
    
   # keys = pygame.key.get_pressed()
    #if keys[pygame.K_a]:
     #   x += speed
    #if keys[pygame.K_d]:
     #   x -= speed
    #if keys[pygame.K_w]:
     #   y -= speed
    #if keys[pygame.K_s]:
         #   y += speed
    
#Soccer ball that another player could control
    pygame.draw.circle(screen, WHITE, (int(x+100), int(y+69)),24) #drwaing the soccer ball 

    pygame.display.update() #update all changes to screen #updates the display 
    