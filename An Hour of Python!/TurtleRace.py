from turtle import Turtle #Import turtle for graphics things
from random import randint #Import random for random stuff

def DrawTrack(numRacers, speed = 40, steps = 42, startX = -400, startY = 350):
    pen = Turtle(shape='triangle', visible=False) ##Create pen to draw track with
    pen.speed(speed)
    pen.speed(25) #Make pen draw faster
    pen.penup() #Lift pen up to avoid drawing lines
    pen.goto(startX, startY) #Move pen to start pos
    
    trackHeight = 60 + (25*numRacers)
    dashes = (int)(trackHeight/40)

    for step in range(steps): #Draw lines for the race track
        pen.write(step, align='center') #Write current step in track
        pen.right(90)
        for _ in range(dashes): ##Create the dashes in the track
            pen.pendown()
            pen.forward(20)
            pen.penup()
            pen.forward(20)
        pen.left(90)
        pen.goto(startX+(20*(step+1)), startY) #Move to next step location

def SetupRaceTurtles(turtles, colors = ['blue', 'pink', 'purple', 'red', 'orange', 'black', 'magenta'], startX = -420, startY = 310): #Setup the racers for a race
    turtleCount = 0
    colorCount = 0
    for turtle in turtles: ##Iterate through racers
        if (colorCount >= len(colors)): #Set color count to 0 when it reaches the last color
            colorCount = 0
        turtle.color(colors[colorCount]) #Set the racers color
        colorCount += 1 #Increment color count by 1

        turtle.penup() #Lift pen up
        turtle.speed(20) #Set the turtles speed to help move them to the start location faster
        turtle.goto(startX, startY-(25*turtleCount)) #Move the racer to its starting location
        turtle.pendown() #Put the pen down to get it ready to race
        turtle.st() #Make the turtle visible again, because we have finished setting it up

        turtleCount += 1 #Increment turtle count by 1


def RaceTurtles(turtles, turns = 280, minStep = 1, maxStep = 5): #Race the turtles
    for _ in range(turns): #Iterate through the amount of turns the turtles have to win the race
        for turtle in turtles: #Iterate through each turtle on the race track
            turtle.forward(randint(minStep, maxStep)) #Move the race forward by a random amount


turtles = [] #Create turtles list to be used later on
numTurtles = 12 #Set the num of turtles in the race

DrawTrack(numTurtles, steps=23, speed=100) ##Draw race track

for _ in range(numTurtles): #Create the racers we are using
    turtles.append(Turtle(shape='turtle', visible=False)) ##Make the racers invisible while we set them up

SetupRaceTurtles(turtles) #Setup the turtles for a race

for turt in turtles: ##Iterate through the turtles to spin them
    turt.speed(10) ##Set the turtles speed back down to a normal value
    turt.right(360) ##Spin to assert dominance

RaceTurtles(turtles, turns=(23*7)) #Race the turtles
input() #Wait for user to input something to exit the program