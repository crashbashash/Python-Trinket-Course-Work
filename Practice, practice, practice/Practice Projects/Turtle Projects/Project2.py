from turtle import Turtle ##Import Turtle for some graphics stuff

def DrawRectangle(pen, xPos = 0, yPos = 0, height = 40, width = 30, lineColor = 'black', fillColor = 'red'): ##Function to draw a square on the screen
    pen.ht() ##Make the pen invisible while setting it up
    pen.penup() ##Lift the pen up to avoid drawing lines when moving it into position
    pen.setheading(0) #Set the heading of the pen to east to prepare it for drawing a square
    pen.color(lineColor) #Set the line color of the pen
    pen.fillcolor(fillColor) #Set the fill color of the pen
    pen.goto(xPos, yPos) #Move the pen to the desired x and y position
    pen.pendown() #Put pen down to begin drawing a square
    pen.st() ##Make the pen visible while drawing the rectangle

    pen.begin_fill() ##Begin the pens fill routine
    #Create 4 lines using the pen
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
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


def DrawHexagon(pen, xPos = 0, yPos = 0, size = 30, lineColor = 'black', fillColor = 'red'): #Function to create a hexagon using a pen
    ang = 360/6 #Set the angle the pen moves at
    pen.ht() ##Make the pen invisible while setting it up
    pen.penup() ##Lift the pen up to avoid drawing lines when setting it up
    pen.setheading(0) #Set the pens heading to prepare it for drawing a circle
    pen.color(lineColor) #Set the pens line color to the desired color
    pen.fillcolor(fillColor) #Set the pens fill color to the desired color
    pen.goto(xPos, yPos) #Move the pen to the desired x and y position
    pen.pendown() #Put the pen down to begin drawing the hexagon
    pen.st() #Make the pen visible while drawing the hexagon

    pen.begin_fill() ##Begin the pens fill routine
    for _ in range(6):
        pen.forward(size) #Move pen forward by a predefined number of pixels
        pen.left(ang) #Move pen left by a predefined angle
    pen.end_fill() ##End the pens fill routine


def DrawShape(pen, xPos = 0, yPos = 0, sides = 5, size = 100, lineColor = 'black', fillColor = 'red'): ##Function to create a pentago using a pen
    pen.ht() ##Make the pen invisible while setting it up
    pen.penup() ##Lift the pen up to avoid drawing lines when setting it up
    pen.setheading(0) #Set the pens heading to prepare it for drawing a circle
    pen.color(lineColor) #Set the pens line color to the desired color
    pen.fillcolor(fillColor) #Set the pens fill color to the desired color
    pen.goto(xPos, yPos) #Move the pen to the desired x and y position
    pen.pendown() #Put the pen down to begin drawing the shape
    pen.st() #Make the pen visible while drawing the shape

    pen.begin_fill() ##Begin the pens fill routine

    for _ in range(sides): ##Create a predefined amount of lines for the shape
        pen.forward(size)
        pen.left(360/sides)

    pen.end_fill() ##End the pens fill routine


pen = Turtle() ##Create turtle pen object
pen.speed(10)

base_x = -400 ##Set the base x pos
base_y = 300 ##Set the base y pos

for i in range(0, 6): ##Create the first line of shapes
    if i % 2 == 0: ##Alternate between squares and circles
        DrawRectangle(pen, base_x + (i * 100), base_y, height=60, width=60, fillColor='green')
    else:
        DrawCircle(pen, (base_x + (i*100))+(30/2), base_y, size=30, fillColor='blue')

base_y = 220 ##Set the base y pos

for i in range(0, 6): ##Create the second line of shapes
    if i % 2 == 0: ##Alternate between triangles and rectangles
        DrawTriangle(pen, xPos=base_x + (i*100), yPos=base_y, size=60, fillColor='red')
    else:
        DrawRectangle(pen, xPos=base_x + (i*100), yPos=base_y, height=60, width=50, fillColor='yellow')

base_y = 140

for i in range(0 , 6): ##Create the third line of shapes
    if i % 2 == 0: ##Alternate between hexagons and pentagons
        DrawShape(pen, xPos=base_x + (i*100), yPos=base_y, sides=6, size=35, fillColor='purple') ##Draw hexagon
    else:
        DrawShape(pen, xPos=base_x + (i*100), yPos=base_y, sides=5, size=35, fillColor='orange') ##Draw pentagon

input() ##Wait for user to exit the program