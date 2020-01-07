from turtle import Turtle ##Import turtle for graphics
from random import randint ##Import randint for random integers

def DrawDashes(pen, length = 600, dashLength = 20, colors = ['blue', 'pink', 'purple', 'black', 'yellow', 'orange']): ##Function to draw dashes in a line
    numDashes = (int)(length / (dashLength*2)) ##Specify the amount of dashes to create
    pen.setheading(0) ##Set pens heading to east

    for _ in range(numDashes): ##Loop through the amount of dashes we need to make
        pen.color(colors[randint(0, len(colors)-1)]) ##Set the pens color to a random color from a predefined list
        pen.pendown() ##Put pen down to make line
        pen.forward(dashLength) ##Create dash with predefines length
        pen.penup() ##Place pen up to stop making lines
        pen.forward(dashLength) ##Move pen to next pos to get ready to make more dashes

    pen.ht() ##Hide pen when finished drawing dashes

pen = Turtle() ##Create a pen object
pen.penup()
pen.goto(-400, 350)

DrawDashes(pen) ##Draw dashes using the pen object

input() ##Wait for user to exit software