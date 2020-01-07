import turtle #Import the turtle module to draw shapes

tina = turtle.Turtle() #Create the "tina" turtle object
tina.shape("turtle") #Set the pens shape to be a turtle

def draw_circle(turtle, line_color, fill_color, size, x, y): #Function to draw circles
    turtle.penup() #Lift pen up to avoid creating a line when moving the pen
    turtle.color(line_color) #Set the line color
    turtle.fillcolor(fill_color) #Set the fill color
    turtle.goto(x, y) #Goto the circles desired position
    turtle.pendown() #Put pen down to start drawing the circle
    turtle.begin_fill() #Start the fill routine
    turtle.circle(size) #Set the size of the circle and draw the circle
    turtle.end_fill() #Stop the fill routine
    turtle.penup() #Lift pen back up to avoid creating lines when you wish to move the pen again

draw_circle(tina, "black", "blue", 35, 50, 75) #Draw right ear
draw_circle(tina, "black", "blue", 35, -50, 75) #Draw left ear
draw_circle(tina, "black", "purple", 50, 0, 0) #Draw face

tina.goto(0,0) #Place the turtle back in the center of the screen

input() #Wait for the user to end the program