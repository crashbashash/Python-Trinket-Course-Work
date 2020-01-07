from turtle import Turtle #Import turtle for graphics stuff

def DrawHexagon(pen, size = 30, colors = ['blue', 'pink', 'purple', 'black', 'red', 'orange']): #Function to create a hexagon using a pen
    ang = 360/6 #Set the angle the pen moves at
    pen.setheading(0) #Set pens heading to east so it's facing the correct direction

    for i in range(6):
        pen.color(colors[i])
        pen.forward(size) #Move pen forward by a predefined number of pixels
        pen.left(ang) #Move pen left by a predefined angle


pen = Turtle() #Create pen object

DrawHexagon(pen) #Draw hexagon using a pen

input() ##Wait for user to exit program