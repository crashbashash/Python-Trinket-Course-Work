from turtle import Turtle, Screen ##Import turtle for graphics stuff

def ChangeScreenColor(color = 'black'):
    screen = Screen()
    screen.bgcolor(color)

def DrawTriangle(pen, xPos = 0, yPos = 0, size = 100, lineColor = 'white', flip = False): ##Function to draw a triangle to the screen
    pen.ht() ##Hide the pen when setting it up
    pen.penup() ##Lift pen up to avoid creating lines
    pen.color(lineColor) ##Set the line color
    pen.setheading(0) ##Set the heading of the pen to east
    pen.goto(xPos, yPos) ##Move to the desired x and y position

    pen.pendown() ##Put pen down to begin drawing
    for _ in range(3): ##Create 3 lines for the triangle
        pen.forward(size)
        if flip:
            pen.right(120)
        else:
            pen.left(120)


pen = Turtle() ##Create pen object

ChangeScreenColor('black') ##Set the screens color
DrawTriangle(pen, xPos=-300, yPos=-300, size=600) ##Draw first triangle
DrawTriangle(pen, xPos=-300, yPos=150, size=600, flip=True) ##Draw second triangle

input() ##Wait for user to exit the program