#I need to use a nested loop to draw a shape
#09/26/18
#CTI-110 P4LAB-Nested Loops
#Leonardo Delgado
#

#import turtle
import turtle

#Specify the shape
star = turtle.Turtle()

#Draw the Star
for draw in range(1):
    star.left(75)
    star.forward(100)
    star.right(130)
    star.forward(100)
    for draw in range(1):
        star.right(150)
        star.forward(110)
        for draw in range(1):
            star.right(150)
            star.forward(100)
            star.right(145)
            star.forward(110)

            
#Import the turtle
#Specify the shape that you want to draw
#Draw the shape of the star
        
