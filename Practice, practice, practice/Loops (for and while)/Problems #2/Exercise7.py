from turtle import Turtle #Import turtle to use graphics stuff

def DrawSpiral(pen, size = 50, ang = 30, speed=10, color = 'blue'): #Draw a spiral using a turtle pen object
    pen.setheading(0) #Set the heading east to begin drawing the spiral
    pen.color(color) #Set the color of the pen
    for i in range (1, size+1): #Create line till the desired spiral size is achieved
        pen.forward(1*i) #Move the pen forward and increase this movement by 1 pixel every step
        pen.left(ang) #Move the pen left by the desired angle to prepare for the next step to be drawn


pen = Turtle() #Create a Turtle object named 'pen'

DrawSpiral(pen, ang=15, size=150) ##Draw a spiral to the screen using the pen Turtle object

input() ##Wait for user to exit the program