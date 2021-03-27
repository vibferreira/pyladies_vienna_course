from turtle import * # built-in library
from math import hypot

bgcolor("#313862") #background color
pen(pencolor = "#E0FF02", fillcolor = "#E0FF02", speed = 6) #pen settings
title("First turtle program") #title of the screen

#equilateral triangle
def eq_triangle(length):
    for i in range(2):
        fd(length)
        lt(120)

#square 
def square (length):
    for i in range(4):
        fd(length)
        lt(90)

#one house
def house(length):
    """ Uses the square and the eq_triangle functions to build a house """
    hypotenuse = hypot(length,length)
    square(length)
    lt(45)
    fd(hypotenuse)
    lt(75)
    eq_triangle(length)
    rt(45)
    fd(hypotenuse)
# house(100)

#village
def village(length, number_of_houses):
    for i in range(number_of_houses):
        house(length)
        rt(-45)
        penup()
        fd(length)
        pendown()

village(50,15)

exitonclick()