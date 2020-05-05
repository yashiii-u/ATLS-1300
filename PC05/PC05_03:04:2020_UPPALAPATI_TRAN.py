#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:00:25 2020

@author: yashi
"""

"""
# 

# PC05 Click Game
Created on Tue Feb 18 12:21:59 2020

@author: Yashi & Michelle :)

This script creates a click game with two goals. Balls are randomly generated and shake 
the goal is to move them to either goal on each side, upon hitting the goal the ball turns red
there is also a count down timer so you have to do it in a certain amount of time.
The last ball always goes on the left side of the goal.
"""

import pygame
import random
from pygame.locals import *
#import time
#import datetime
#import timeit


#define color variables up here
black = (0,0,0)
white = (255,255,255)
lavender = (230,230,250)
pygame.init() #initialize all the pygame functions so it actually DOES stuff.

#create screen and useful variables
screen = pygame.display.set_mode((800,800))
Run = True
drag = False #boolean that determines if dragging happens
x = 400 #where we want to draw stuff
y = 400
r = 25 #how big we want things to be
step = 10 #dis makes it shake
hit = False
selected = 0
#clock = pygame.time.Clock()

#time = 0  #In Seconds


#create Rect for our circle. The pygame Rect has a bunch of cool stuff added to it 
#that will later let us do collisions and the like.
#let's create a Rect that will sit underneath our circle
numCirc = 10
rectList = [] #for storing rect objects
for i in range(numCirc):
    rectList.append(pygame.Rect(random.randint(150,600),random.randint(150,500),r*2,r*2)) #we're setting a rectangle underneath our circle
#the r is the circle  RADIUS, but we want the rect with to be equal to DIAMETER, so:
#diameter = radius * 2

while Run: #start the game loop!
    goal1 = pygame.draw.rect(screen,pygame.Color(230,230,250),(0,250,70,350))
    goal2 = pygame.draw.rect(screen,pygame.Color(230,230,250),(730,250,90,350))
   #from the assginment 
   #tried to debug it but coudln't.
   
   
    start_ticks=pygame.time.get_ticks() #starter tick
    run = True


    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    if seconds>10: # if more than 10 seconds close the game
        break
    print (seconds) #print how many seconds
                
    for event in pygame.event.get(): #scan all events --things happening outside python (mouse and keyboard actions)
        if event.type == pygame.QUIT:
            pygame.quit() #add a quit function so it stops up background tasks
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #get our x and y positions of where the click happened
            for i in range(numCirc):
                if rectList[i].collidepoint(pos[0],pos[1]):
                    drag = True #whenever the mouse is down, we can potentially drag our shape. Word.
                    selected = i
                    print(selected)
                    offsetX = rectList[i].x - pos[0] #let's calculate the difference between where the rectangle is and where the click happened
                    offsetY = rectList[i].y - pos[1]
            
        elif event.type == pygame.MOUSEMOTION:
            if drag: #remember drag is a boolean, and if statements want to know if something is true or not...so we can just pass our variable here!
                pos = event.pos #update position as mouse moves around
                #update the position of the shape based on where the mouse motion event is happening (where the cursor is)
                rectList[selected].x = pos[0] + offsetX 
                rectList[selected].y = pos[1] + offsetY
                

                
            
            
        elif event.type == pygame.MOUSEBUTTONUP: #ok, now we're done dragging, so we want to detect when the mouse button is released.
            drag = False #we can set our boolean to false, so we can't update our Rect position.
    
    speed = [random.randint(-step,step),random.randint(-step,step)] #randome displacement to add fun wiggles to our circle. 
    
    
    
    screen.fill(black) #draw/redraw the screen to "erase" previous drawings
    
    goal1 = pygame.draw.rect(screen,pygame.Color(230,230,250),(0,250,70,350))
    goal2 = pygame.draw.rect(screen,pygame.Color(230,230,250),(730,250,90,350))
                                                 
    for i in range(numCirc):
        if (rectList[selected].colliderect(goal1)): #the circles in the array are checked to see if the goals are within the selected one's boundaries
            hit = True
            selectedCir = selected
            g = 1
        elif (rectList[selected].colliderect(goal2)): #the circles in the array are checked to see if the goals are within the selected one's boundaries
            hit = True
            selectedCir = selected
            g = 2
            
        
    if(hit):      
        screen.fill(black)   
        goal1 = pygame.draw.rect(screen,pygame.Color(230,230,250),(0,250,70,350))
        goal2 = pygame.draw.rect(screen,pygame.Color(230,230,250),(730,250,90,350))                                     
        pygame.draw.circle(screen, pygame.Color(255,0,0), (rectList[selectedCir].x,rectList[selectedCir].y),r)
                                 
        if g == 1:                                        
            rectList[selectedCir].clamp_ip(goal1) 
            pygame.draw.circle(screen, pygame.Color(230,230,250), (rectList[selectedCir].x,rectList[selectedCir].y),r)
        elif g == 2:
            rectList[selectedCir].clamp_ip(goal2)                                        
        hit = False
        #draw/redraw the screen to "erase" previous drawings
        
        for i in [x for x in range(numCirc) if x != selectedCir]:
            pygame.draw.circle(screen, (lavender), (rectList[i].x+r + speed[0], rectList[i].y+r+speed[1]), r) #(x+randint(-3,3), y+randint(-3,3) ), 15)
        
        
    else:
        #now let's draw the circle object on top of our rectangle                                             
        for i in range(numCirc):
            pygame.draw.circle(screen, (lavender), (rectList[i].x+r + speed[0], rectList[i].y+r+speed[1]), r) #(x+randint(-3,3), y+randint(-3,3) ), 15)
            

   

  




#x=0
#while x < 10:
 #   x+=1
  #  pygame.time.delay(1000)


    
    pygame.display.update() #update our image to our screen