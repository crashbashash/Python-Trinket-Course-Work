import turtle #Import turtle to create shapes
import random #Import random for some fun

sides = 8

tina = turtle.Turtle() #Create the "tina" turtle object
tina.shape("turtle") #Set the pens shape to a turtle

color_list = ['red', 'green', 'yellow', 'blue', 'pink', 'purple', 'black', 'magenta'] #Create the list of colors

tina.fillcolor(color_list[random.randint(0, len(color_list)-1)])
random.shuffle(color_list) #Randomise the list of colors

tina.begin_fill()
for color in color_list: #Iterate through the color list
    tina.color(color) #Set tinas color to the current color
    tina.forward(100) #Move tina forward 100 pixels
    tina.left(360/sides) #Turn tina left by 90 degrees
tina.end_fill()

input() #Wait for the user to exit the program