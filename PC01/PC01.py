"""
# PC01 - GRAFFITI

# Uppalapati

# 01/29/2020

#

# Description - Turtle draws flower using petals on a flower wall backgroud

@author: yashi
"""

from turtle import * 
jd = Screen()

jd.screensize(700,500)
jd.bgcolor("black")


jd.bgpic("python-flowers.gif")
jd.update()

c = Turtle()
#c.color('black')
#c.shape('circle')
#c.width(1)

for i in range(13) :
  c.up()
  c.goto(-100,-100)
  c.down()
  c.fillcolor('#B370B0')
  c.begin_fill()
  c.circle(200,70)
  c.left(110)
  c.circle(200,70)
  c.end_fill()

c.hideturtle()
done()

#https://medium.com/groklearning/turtle-flowers-coding-project-b2af6ffd1a30
