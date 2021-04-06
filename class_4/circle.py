from turtle import *
from math import pi

bgcolor("#313862") #background color
pen(pencolor = "#E0FF02", fillcolor = "#E0FF02", speed = 6) #pen settings
title("Second turtle program") #title of the screen

#n side polygon 
def polygon (length, number_of_sides):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        fd(length)
        lt(angle)

#circle 1:
circle(50)

#circle 2:
def circle_2 (radius):
    circun = (2*radius*pi)
    number_of_sides = 50 #not very sure how to define the number of sides of a circle, should it depend on the cinrcunference?
    length = circun/number_of_sides
    polygon(length, number_of_sides)

circle_2(50)

exitonclick()