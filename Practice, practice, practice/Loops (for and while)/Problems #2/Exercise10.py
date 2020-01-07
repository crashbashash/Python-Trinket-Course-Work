from turtle import Turtle ##Import turtle for graphics stuff
from random import randint ##Import randint for some random fun

def StampRandomLoc(pen, minX = -400, maxX = 400, maxY = 350, minY = -350, shape = 'turtle', color = 'pink', amount=100): ##Function to stamp random locations on the screen
    pen.shape(shape) ##Set the shape of the pen
    pen.color(color) ##Set the color of the pen
    pen.penup() ##Put pen up to avoid creating lines
    pen.ht() ##Make the pen invisible

    for _ in range(amount): ##Create stamps of a predefined quantity
        xPos = randint(minX, maxX) #Calculate the x pos to move the pen to
        yPos = randint(minY, maxY) #Calculate the y pos to move the pen to
        pen.goto(xPos, yPos) #Move the pen to the random positon
        pen.stamp() #Stamp the screen with the pen


pen = Turtle() ##Create a turtle object

StampRandomLoc(pen) ##Stamp random locations on the screen using the pen object

input('Hit enter to exit') ##Wait for user to exit out of the program