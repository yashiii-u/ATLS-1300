#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# PC01 - GRAFFITI

# Uppalapati

# 01/29/2020

#

# Description - Turtle draws flower using petals on a flower wall backgroud

@author: yashi
"""

from turtle import *  #imports turtle
jd = Screen() #defines the screen size as jd

jd.screensize(700,500) #sets the screensize
jd.bgcolor("black") #sets the background color


jd.bgpic("python-flowers.gif") #this imports the background 
jd.update()#updates the screen

c = Turtle() #defining the turtle 
#c.color('black')
#c.shape('circle')
#c.width(1)

for i in range(13) : #how many times it draws the petal 
  c.up() #pen to lift up
  c.goto(-100,-100) #goes to the set coordinates to start drawing
  c.down() #can draw with this setting
  c.fillcolor('#B370B0') #giving it what color to draw
  c.begin_fill() #starts to fill the petals
  c.circle(200,70) #draws a half cirlce to create the flower
  c.left(110) #turns left after being done to draw more
  c.circle(200,70) #draws a half circle to create the petal
  c.end_fill() #finsihes the job

c.hideturtle() #hides the turtle
done() #stops the function 










