from turtle import *

bgcolor("#313862") #background color
pen(pencolor = "#E0FF02", fillcolor = "#E0FF02", speed = 6) #pen settings
title("Second turtle program") #title of the screen

number_of_sides = int(input("Input number of sides of a polygon: "))

def polygon (length):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        fd(length)
        lt(angle)

polygon(50)

exitonclick()