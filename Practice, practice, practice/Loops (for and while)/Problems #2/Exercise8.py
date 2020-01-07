from turtle import Turtle ##Import turtle for graphics stuff

def DrawStampSpiral(pen, stepOffset = 1.7, spacing = 1.6, size = 100, ang = 15, speed=10, color = 'blue', shape = 'circle'): #Draw a stamp spiral using a turtle pen object
    pen.setheading(0) #Set the heading east to begin drawing the spiral
    pen.color(color) #Set the color of the pen
    pen.penup() #Put pen up so we don't draw lines
    pen.shape(shape) ##Set the shape of the pen
    for step in range (1, size+1): #Create line till the desired spiral size is achieved
        pen.stamp() #Create a stamp before moving to the next step
        moveBy = spacing * step/stepOffset ##Calculate how much the pen should move by
        pen.forward(moveBy) #Move the pen forward and increase this movement by 1 pixel every step
        pen.left(ang) #Move the pen left by the desired angle to prepare for the next step to be drawn


pen = Turtle() #Create a turtle object

DrawStampSpiral(pen) ##Draw stamp using the pen turtle object

input() ##Wait for user to exit the program