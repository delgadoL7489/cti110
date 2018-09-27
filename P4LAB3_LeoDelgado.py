#The program draws a snowflake
#09/26/18
#CTI-110 P4T1c-Snowflake
#Leonardo Delgado
#

#import turtle
import turtle

#Get specifics
snowflake = turtle.Turtle()
snowflake.color('blue')

#Start drawing
snowflake.right(90)

for snow in range(6):
    snowflake.forward(100)
    snowflake.forward(-40)
    snowflake.left(40)
    snowflake.forward(35)
    snowflake.forward(-35)
    snowflake.right(80)
    snowflake.forward(35)
    snowflake.forward(-35)
    snowflake.left(40)
    snowflake.forward(-60)
    snowflake.left(60)

#Import turtle
#Get the specifics for the snowflake
#Draw the shape
