#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# PC02 - ANIMATION

# Uppalapati

# 02/03/2020
# Description - Turtle draws circle lines in different colors 

@author: yashi
"""
from turtle import * #import turtle
Jd = Turtle() #defining the turtle
Jd.speed(9) #speed on how fast it draws
colors = ['#F4DBD8', '#BEA8A7', '#C09891', '#775144', '#2A0800', '#C09891'] #range of colors to choose from
for x in range(90): #how many loops it goes for
    pencolor(colors[x % 3]) #chooses from the colors/defining the pen color
    width(x / 100 + 1) #setting the width of the draing 
    forward(x)
    left(59) #goes left
    
    #repeats the steps from above
from turtle import * 
oop = Turtle()
oop.speed(10)
colors = ['#C6D8FF', '#71A9F7', '#6B5CA5', '#72195A', '#4C1036', '#6B5CA5']
for x in range(90):
    pencolor(colors[x % 2])
    width(x / 100 + 1)
    forward(x)
    right(59)
    
  #repeats th esteps from above
from turtle import *
haha = Turtle()
haha.speed(9)
colors = ['#172121', '#444554', '#7F7B82', '#BFACB5', '#E5D0CC', '#7F7B82']
for x in range(90):
    pencolor(colors[x % 3])
    width(x / 100 + 1)
    forward(x)
    left(59)
    
    #repeats the steps from above
from turtle import *
lol = Turtle()
lol.speed(10)
colors = ['#083D77', '#EBEBD3', '#F4D35E', '#EE964B', '#F95738', '#F4D35E']
for x in range(90):
    pencolor(colors[x % 2])
    width(x / 100 + 1)
    forward(x)
    right(59)
    
Jd.hideturtle() #hides turtle 
oop.hideturtle()#hides turtle 
haha.hideturtle()#hides turtle 
lol.hideturtle()#hides turtle 

done() #updates everything 

