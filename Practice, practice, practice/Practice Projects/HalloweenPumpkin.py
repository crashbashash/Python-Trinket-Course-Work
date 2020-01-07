from turtle import Turtle, Screen ##Import turtle for graphics stuff and screen to manipulate turtles screen

def SetScreenColor(color = 'orange'):
    screen = Screen()
    screen.bgcolor(color)

def DrawSquare(pen, xPos = 0, yPos = 0, size = 30, lineColor = 'black', fillColor = 'red'): ##Function to draw a square on the screen
    pen.ht() ##Make the pen invisible while setting it up
    pen.penup() ##Lift the pen up to avoid drawing lines when moving it into position
    pen.setheading(0) #Set the heading of the pen to east to prepare it for drawing a square
    pen.color(lineColor) #Set the line color of the pen
    pen.fillcolor(fillColor) #Set the fill color of the pen
    pen.goto(xPos, yPos) #Move the pen to the desired x and y position
    pen.pendown() #Put pen down to begin drawing a square
    pen.st() ##Make the pen visible while drawing the square

    pen.begin_fill() ##Begin the pens fill routine
    for _ in range(4): #Create 4 lines using the pen
        pen.forward(size)
        pen.left(90)
    pen.end_fill() ##End the pens fill routine

def DrawCircle(pen, xPos = 0, yPos = 0, size = 30, lineColor = 'black', fillColor = 'red'): ##Function to draw a circle on the screen
    pen.ht() ##Make the pen invisible while setting it up
    pen.penup() ##Lift the pen up to avoid drawing lines when setting it up
    pen.setheading(0) #Set the pens heading to prepare it for drawing a circle
    pen.color(lineColor) #Set the pens line color to the desired color
    pen.fillcolor(fillColor) #Set the pens fill color to the desired color
    pen.goto(xPos, yPos) #Move the pen to the desired x and y position
    pen.pendown() #Put the pen down to begin drawing the circle
    pen.st() #Make the pen visible while drawing the circle

    pen.begin_fill() ##Begin the pens fill routine
    pen.circle(size) #Draw a circle with the desired size
    pen.end_fill() ##End the pens fill routine

def DrawTriangle(pen, xPos = 0, yPos = 0, size = 50, lineColor = 'black', fillColor = 'red'): ##Function to draw a triangle on the screen
    pen.ht() ##Make the pen invisible while setting it up
    pen.penup() ##Lift the pen up to avoid drawing lines when setting it up
    pen.setheading(0) #Set the pens heading to prepare it for drawing a circle
    pen.color(lineColor) #Set the pens line color to the desired color
    pen.fillcolor(fillColor) #Set the pens fill color to the desired color
    pen.goto(xPos, yPos) #Move the pen to the desired x and y position
    pen.pendown() #Put the pen down to begin drawing the triangle
    pen.st() #Make the pen visible while drawing the triangle

    pen.begin_fill() ##Begin the pens fill routine
    for _ in range(3): ##Draw a triangle
        pen.forward(size)
        pen.left(120)
    pen.end_fill() ##End the pens fill routine

def DrawTShape(pen, xPos = 0, yPos = 0, height = 150, width = 120, lineColor = 'black', fillColor = 'red'): ##Function to draw a T shape on the screen
    pen.ht() ##Make the pen invisible while setting it up
    pen.penup() ##Lift the pen up to avoid drawing lines when setting it up
    pen.setheading(0) #Set the pens heading to prepare it for drawing a circle
    pen.color(lineColor) #Set the pens line color to the desired color
    pen.fillcolor(fillColor) #Set the pens fill color to the desired color
    pen.goto(xPos, yPos) #Move the pen to the desired x and y position
    pen.pendown() #Put the pen down to begin drawing the T shape
    pen.st() #Make the pen visible while drawing the T shape

    pen.begin_fill() ##Begin the pens fill routine

    pen.forward(width*0.25) #Make the base of the T shape
    pen.left(90)
    pen.forward(height*0.8) #Make the right stem of the T shape
    pen.right(90)
    pen.forward(width*0.375) #Make the right base of the head of the T shape
    pen.left(90)
    pen.forward(height*0.2) #Move up
    pen.left(90)
    pen.forward(width) #Move left
    pen.left(90)
    pen.forward(height*0.2) #Move down
    pen.left(90)
    pen.forward(width*0.375) #Move right
    pen.right(90)
    pen.forward(height*0.8) #Make the left stem of the T shape

    pen.end_fill() ##End the pens fill routine


pen = Turtle(shape='arrow') ##Create the pen object and set its shape
pen.pensize(1) ##Set the size of the pen

SetScreenColor() ##Set the color of the screen

DrawCircle(pen, xPos=-300, yPos=70, size=130) ##Draw a circle to the screen
DrawSquare(pen, xPos=100, yPos=70, size=250) ##Draw a square to the screen
DrawTriangle(pen, xPos=-430, yPos=-350, size=280) ##Draw a triangle to the screen
DrawTShape(pen, xPos=180, yPos=-350, height=300, width=280) ##Draw a T Shape to the screen


input() ##Wait for the user to end the program