from turtle import forward, left, penup, pendown, exitonclick

#draws a square
# for i in range(4):
#     forward(100)
#     left(90)  

#draws a retangle
# for i in range(2):
#     forward(100)
#     left(90)
#     forward(50)
#     left(90)

#draws 3 squares rotated by 20º
# def square_angle20 ():
#     for i in range (4):
#         forward(100)
#         left(90)
#     left(20)
        
# square_angle20 () # how to refactor the function to only need to call it once 
# square_angle20 ()
# square_angle20 ()

#draws a discontinous line
for i in range(20):
    forward(2)
    penup()
    forward(5)
    pendown()  
    
exitonclick()