#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:03:15 2020
# PC10 API In the Sky
@author: Yashi & Michelle :)
    
Descritpion : Uses Coronavirus data from all the countries and loops them into how many cases and how many deaths
there has been in every country. This animation changes every two seconds to a diffrent country and the representation 
is done by a pie chart. Blue resembles the number of cases and pink represents the number of deaths in each country. We made sure these
colors were color-blind friendly for trianopia.
        
        
"""
#code used from PC10 skeleton but modified in accordance to data we used

import pygame #imports all the random functions so we can use them.# math library, yay! use np.____ to access the stuff in this library#accesses online data
import requests
import math
import numpy
import time
pygame.init()

#set up our screen (global variables)
screen = pygame.display.set_mode((600,600)) 
screen.fill((0,0,0))

#import data GLOBAL variable with website!!
URL = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json/'  #coronavirus data

#create classes
#use API data Coronavirus statistics
class countryCovidStats:
  def __init__(self,screen): #special method that runs when we instantiate our object
    self.data=[] #our data will automatically get stored here when we run self.updatData in the next line
    self.refreshsec=2
    self.textcolor=(255,255,255)
    self.textsize=40
    self.pieColor1=(50,161,174) #colorblind friendly blue
    self.pieColor2=(255,91,97) #colorblind friendly pink
    self.country,self.cases,self.percdeaths= self.updateData() #store the temp data to self.radius
    self.screen=screen
#create objects/inital conditions/local variables

  def updateData(self, URL=URL):
    '''Pulls data from URL (API only) and parses it into a data dictionary.
    You should update this function to parse your own code!'''
    #Pull data from the URL
    self.data = requests.get(URL).json() #pull data from your URL
    
    #create data variable with values you want to work with. You may want to make more than one.. 
    #Here we'll just use temp
    # we used country, cases, percdeaths, prevcountry, cases count, deaths count
    country=[]
    cases=[]
    percdeaths=[]
    prevcountry=""
    casescount=0
    deathscount=0
    perc=0.0
    loopcounter=0
    for datapoint in self.data["records"]: #pulls data from records
        loopcounter += 1 #loop indexed info
        if datapoint["countriesAndTerritories"] == prevcountry:
            casescount += int(datapoint["cases"]) #display data as "cases"
            deathscount += int(datapoint["deaths"]) #display data as "deaths"
        else:
            country.append(datapoint["countriesAndTerritories"])
            if prevcountry != "":
                cases.append(casescount)
                if casescount > 0:
                    perc=round(100.0*float(deathscount)/float(casescount),2) #my dad helped 
                    percdeaths.append(perc)
            casescount = int(datapoint["cases"]) #find da data and turn it into the number
            deathscount = int(datapoint["deaths"])
            perc=0.0 #bool make it percentage 
            prevcountry=datapoint["countriesAndTerritories"]
    cases.append(casescount)
    if casescount > 0: #if it's more than zero then do some math
        perc=round(100.0*float(deathscount)/float(casescount),2) #math for percentage
        percdeaths.append(perc)         #percentage
    return country, cases, percdeaths
     #sets font
  def drawText(self, label, xloc, yloc, fontsize, fontcolor):
     font = font = pygame.font.Font('freesansbold.ttf', fontsize) 
     text = font.render(label, True, fontcolor) 
     textRect = text.get_rect()
     textRect.center = (xloc, yloc) 
     screen.blit(text, textRect) #draw text
     # draw the pi chart - pygame.org
  def drawPie(self, perc, width=150, x=300, y=350):
      pygame.draw.circle(self.screen,(50,161,174),(x, y),width)
      numarcs=15
      arcgap=width//numarcs
      PI=math.pi
      for i in range(1,numarcs):
          pygame.draw.arc(self.screen,(255,91,97),[x-(width-(i-1)*arcgap), y-(width-(i-1)*arcgap), 2*(width-(i-1)*arcgap), 2*(width-(i-1)*arcgap)], 0, PI*perc/float(50), 10)
          #fill it in 
  def draw(self, id):
     screen.fill((0,0,0))
     self.drawText((self.country[id]).replace("_"," "), 300, 50, 40, (255,255,255)) #display country name at the top in white
     self.drawText("Cases = "+str(self.cases[id]), 150, 120, 30, (50,161,174)) #makes cases color blue
     self.drawText("Deaths = "+str(self.percdeaths[id])+"%", 400, 120, 30, (255,91,97)) #make death color pinkish
     self.drawPie(self.percdeaths[id]) #draw the pie chart
    
#create object
chartdata = countryCovidStats(screen) #our object only has one required 
#starter tick
refreshsecs=2
numtimes=len(chartdata.country)
run=True
#runs everything
while run:
    for i in range(1,numtimes): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False# mainloop
        chartdata.draw(i)
        pygame.display.update()
        time.sleep(refreshsecs)#calculate how many seconds

            
     #print how many seconds

pygame.quit()