#I have to make my initials using turtle
#09/24/13
#CTI-110 P4T1b-Initials
#Leonardo Delgado
#

#Import the turtle
import turtle

#Get specific design for L
first_initial = turtle.Turtle()
first_initial.color("Red")
first_initial.pensize(5)

#Draw the letter L
first_initial.penup()
first_initial.backward(100)
first_initial.pendown()
first_initial.right(90)
first_initial.forward(200)
first_initial.left(90)
first_initial.forward(100)

#Get specifics for D
last_initial = turtle.Turtle()
last_initial.color("Blue")
last_initial.pensize(5)

#Draw the letter D
last_initial.penup()
last_initial.forward(100)
last_initial.right(90)
last_initial.forward(200)        
last_initial.pendown()
last_initial.left(180)
last_initial.forward(200)
last_initial.right(130)
last_initial.forward(180)
last_initial.right(110)
last_initial.forward(160)

#Import turtle
#Set the design parameters for the L
#Set the directions to draw the letter L
#Set the design parameters for the D
#Set the directions to draw the letter D

