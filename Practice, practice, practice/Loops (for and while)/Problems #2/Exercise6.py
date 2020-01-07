from turtle import Turtle ##Import turtle for graphics
from random import randint ##Improt random for random stuff

def DrawDashes(pen, rows = 2, length = 600, dashLength = 20, colors = ['blue', 'pink', 'purple', 'black', 'yellow', 'orange']): ##Function to draw dashes in a line
    for i in range(rows):
        numDashes = (int)(length / ((dashLength*(i+1))*2)) ##Specify the amount of dashes to create
        pen.setheading(0) ##Set pens heading to east
        for _ in range(numDashes): ##Loop through the amount of dashes we need to make
            pen.color(colors[randint(0, len(colors)-1)]) ##Set the pens color to a random color from a predefined list
            pen.pendown() ##Put pen down to make line
            pen.forward((dashLength*(i+1))) ##Create dash with predefines length
            pen.penup() ##Place pen up to stop making lines
            pen.forward((dashLength*(i+1))) ##Move pen to next pos to get ready to make more dashes
            
        ##Move pen back for next row
        pen.setheading(180) ##Set heading to west
        pen.forward(length) ##Move pen back to base pos
        pen.left(90)
        pen.forward(20)


    pen.ht() ##Hide pen when finished drawing dashes

pen = Turtle() #Create pen object
pen.penup()
pen.goto(-400, 300) ##Move pen to pos

DrawDashes(pen) ##Draw dashes to pen object

input() ##Wait for user to exit software