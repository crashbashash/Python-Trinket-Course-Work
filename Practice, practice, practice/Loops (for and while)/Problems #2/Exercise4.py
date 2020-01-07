from turtle import Turtle #Import turtle for graphics stuff

def DrawOctagon(pen, size = 20, colors = ['blue', 'red', 'orange', 'green', 'yellow', 'pink', 'purple', 'black', 'magenta']): ##Function to draw octagons
    ang = 360/8 ##Set angle to move pen by
    pen.setheading(0) #Set pens heading to east

    for i in range(8): ##Loop through all the sides of an octagon
        pen.color(colors[i])
        pen.forward(size) ##Move pen forward by predefined size
        pen.left(ang) ##Move pen left by a predefined angle
    
    pen.ht() ##Hide pen when done to show off the beauty of the shape


pen = Turtle() ##Create the pen object

DrawOctagon(pen) ##Draw octagon using the pen object
input() ##Wait for user to exit application