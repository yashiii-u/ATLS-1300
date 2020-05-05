#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
# 
# PC08/09 Redo
Created on Mon March 18 11:09:03 2020
@author: Michelle & Yashi
Description: Speaker from the 60's- plays groovy music and circles grow as the
"bass" of the music- moves to the beat of the shakers in the background
rotates through colors picked to contrast blue speakers- kind of gives a psychedelic 
feel- hurts eyes tho so be careful - music stops when screen fills blue again.
- inspired by target commerical
"""


import pygame
#import numpy as np
from random import *
pygame.init() #initializes everything 

#global
size = (500,500) #screensize
screen = pygame.display.set_mode(size) #sets screen size
clock= pygame.time.Clock() #tracks time
run = True

r1 = 15 #circ radius
r2 = 15
r3 = 15
r4 = 15
r5 = 15
NavyBlue = (0,0,128) #speaker color


screen.fill(NavyBlue) #create background

#add music
pygame.mixer.music.load('FunkyToons.wav') #plays funky toons from zapsplat.com
pygame.mixer.music.play(2) #loop musica 2x


def drawCircle(r,x,y):
    for i in range(12):
        color = (randint(200,255),randint(200,255),randint(0,255))
        pygame.draw.circle(screen,color,(x,y),r)
        
def drawCircle5(r,x,y):
    for i in range(12):
        color5 = (0,0,128)
        pygame.draw.circle(screen,color5,(x,y),r)

# not needed
#def drawCircle2(r,x,y):
#    color = (randint(0,150),randint(0,150),randint(0,150))
#    pygame.draw.circle(screen,color,(x,y),r)
#
#def drawCircle3(r,x,y):
#    color = (randint(0,200),randint(0,200),randint(0,200))
#    pygame.draw.circle(screen,color,(x,y),r)
#    
#def drawCircle4(r,x,y):
#    color = (randint(0,250),randint(0,250),randint(0,250))
#    pygame.draw.circle(screen,color,(x,y),r)
#    
#def drawCircle5(r,x,y):
#    pygame.draw.circle(screen,(0,0,128),(x,y),r)
   

thres = randint(0,100)


#animation starts
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            

#    screen.fill(NavyBlue)
    drawCircle(r1,250,250)# circle 1
# increase circle by one
    r1+=1 
    if r1 >=thres:
         drawCircle(r2,250,250) #second circle
         r2 +=1
    if r2 >=thres:
         drawCircle(r3,250,250) #circle 3
         r3+=1
    if r3 >=thres:
         drawCircle(r4,250,250) #circle 4
         r4+=1
    if r4 >=thres:
         drawCircle(r5,250,250) #circle 5
         r5+=1
    
    drawCircle5(r5,250,250) #dis the blue dot
    
    
    clock.tick(14) #speed
    
      
    pygame.display.update()
  
    
    
pygame.quit()