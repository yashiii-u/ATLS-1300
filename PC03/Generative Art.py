#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Uppalapati

# 01/29/2020



# Description - Turtle draws hexagons making a honeycomb type of strutcre 



"""

from turtle import * #import turtle
lol = Turtle() #define the turtle

from random import randint #import random


size = 10 #set size
circles = 5 #set circles
lol.speed(0) #set speed


colormode(255) #colors 

def move(length, angle): #define length and angle to use later int he code
                lol.right(angle)
                lol.forward(length)

def hex(): #define hex
        lol.pendown() #draw command
        lol.color( randint(0,255),randint(0,255),randint(0,255) ) #randome colors
        lol.begin_fill() #starts to fill
        for i in range(6): #loops 6 times
                move(size,-60) #coordiantes
        lol.end_fill() #end fill
        lol.penup() #done drawing

 
lol.penup() #draw command

for circle in range (circles): #define circles
        if circle == 0: 
                hex() #pulling the def hex()
                move(size,-60) #where it mves
                move(size,-60) #where it moves
                move(size,-60) #where it moves
                move(0,180) #whwere it moves
        for i in range (6): #loops 6 
                move(0,60) #moves to the corrdinate
                for j in range (circle+1): #adds on to the hex
                        hex()
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)
        
        #deifned above
        def move(length, angle):
                lol.right(angle)
                lol.forward(length)
#defiened above
def hex():
        lol.pendown()
        lol.color( randint(0,255),randint(0,255),randint(0,255) )
        lol.begin_fill()
        for i in range(6):
                move(size,-60)
        lol.end_fill()
        lol.penup()


lol.penup()
#defined above
for circle in range (circles):
        if circle == 0:
                hex()
                move(size,-60)
                move(size,-60)
                move(size,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (circle+1):
                        hex()
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)
        
        def move(length, angle):
                lol.right(angle)
                lol.forward(length)
#defined above
def hex():
        lol.pendown()
        lol.color( randint(0,255),randint(0,255),randint(0,255) )
        lol.begin_fill()
        for i in range(6):
                move(size,-60)
        lol.end_fill()
        lol.penup()


lol.penup()
#deifned above
for circle in range (circles):
        if circle == 0:
                hex()
                move(size,-60)
                move(size,-60)
                move(size,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (circle+1):
                        hex()
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)

lol.hideturtle() #hides turtle




#https://medium.com/@benthecoder07/honeycomb-with-python-turtle-52cb0939d125
