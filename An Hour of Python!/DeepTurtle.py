from turtle import Turtle, Screen
import random

def ChangeWindowColor(color = 'white'):
    window = Screen()
    window.bgcolor(color)

def DrawLines(turtles = 8, ang = 360, colors = ['blue', 'red', 'orange', 'black'], shapes = ['classic', 'circle', 'turtle', 'triangle'], draw = True, stamp = True):
    pens = [] #Pens list
    shapeCount = 0
    for _ in range(0,turtles): #Create pen objects
        if shapeCount >= len(shapes): ##Iterate through shapes and make sure not to go above the max length of the shapes list
            shapeCount = 0
        pens.append(Turtle(visible=False, shape=shapes[shapeCount])) ##Create pen
        shapeCount += 1 #Increase shape counter by 1
    
    moveBy = ang/turtles
    count = 0
    colorCount = 0
    for pen in pens: #Move pen objects
        if not draw:
            pen.penup()

        ##Set color of pen
        if colorCount >= len(colors):
            colorCount = 0
        pen.color(colors[colorCount])
        colorCount += 1

        ##Move pen
        pen.left(moveBy*count)
        pen.forward(100)
        
        if stamp: ##Show or hide pen before moving it forward
            pen.stamp()

        count += 1

ChangeWindowColor('yellow')
DrawLines(turtles=16, colors=['pink', 'purple', 'red', 'blue', 'orange', 'magenta'], draw=False)
input()