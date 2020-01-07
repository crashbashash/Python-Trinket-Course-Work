from turtle import Turtle, Screen #Import turtle for graphics stuff

def DrawSquare(pen, size = 50, colors=['black', 'red', 'pink', 'purple']): #Function to create squares with pens
    if pen != None: #Make sure pen is not set to None
        for i in range(4): #Create square with pen
            pen.color(colors[i])
            pen.forward(size)
            pen.left(90)



screen = Screen()
screen.bgcolor('blue') #Change color of the turtle screen

pen = Turtle() #Create pen object
pen.color("black")
pen.shape("turtle")

DrawSquare(pen) #Draw square using a pen

input() #Wait for user to exit software