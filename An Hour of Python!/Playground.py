from turtle import Turtle, Screen #Import turtle to create shapes on the screen and imort screen to get the size of the Turtle window
from time import sleep #Import sleep to allow the script to wait a set amount of seconds
import os #Import os to use console commands
import random #Import random to be used for the mickey function

tina = Turtle() #Create the "tina" Turtle object
tina.shape("turtle") #Set the "tina" Turtle objects pen shape to be a turtle#

def draw_circle(turt, line_color, fill_color, size, x, y): #Function used to draw circles to the screen
    turt.penup() #Place pen up to avoid creating a line when moving the pen
    turt.color(line_color) #Set the pens line color
    turt.fillcolor(fill_color) #Set the pens fill color
    turt.goto(x, y) #Goto the desired x and y coords
    turt.pendown() #Place pen down to begin drawing a line
    turt.begin_fill() #Begin the pens fill routine
    turt.circle(size) #Tell the pen to draw a circle of a set size
    turt.end_fill() #End the pens fill routine once it has created a circle
    turt.penup() #Life the pen up to avoid creating lines if the pen gets moved again

def draw_square(turt, line_color, fill_color, size, x, y): #Function to draw a squard
    turt.penup() #Lift pen up to avoid creating a line when moving the pen
    turt.color(line_color) #Set pens line color
    turt.fillcolor(fill_color) #Set pens fill color
    turt.goto(x, y) #Move pen to desired coords
    turt.pendown() #Put pen down to start drawing lines
    turt.begin_fill() #Begin the pens fill routine
    
    #Create sides
    for _ in range(0,4): #Iterate through a for loop 4 times to create 4 sides
        turt.forward(size) #Move the pen forward by the size specified
        turt.left(90) #Turn the pen left by 90 degrees to start the next line
    
    turt.end_fill() #End the pens fill routine
    turt.penup() #Lift pen back up to avoid creating lines if the pen gets moved


def draw_mickey(turt, line_color, fill_color, x, y): #Function to draw mickey the mouse
    #Draw mickey
    draw_circle(turt, line_color, fill_color, 35,  x+50, y+75) #Draw right ear
    
    draw_circle(turt, line_color, fill_color, 35, x-50, y+75) #Draw left ear

    draw_circle(turt, line_color, fill_color, 50, x, y) #Draw face

def challenge3():
    print ("Polka dot challenge")

    base_x = -300
    base_y = -300

    for _ in range(0, 5):
        base_x = -300
        for _ in range(0, 5):
            draw_circle(tina, "black", "purple", 50, base_x, base_y) #draw circle at pos
            base_x += 130
        base_y += 130

    sleep(3) #Wait 3 seconds before closing the turtle window
    tina.clear()

def challenge4():
    draw_square(tina, "green", "white", 100, 0, 0)
    draw_circle(tina, "blue", "white", 50, 50, 0)
    draw_square(tina, "red", "white", 70, 15, 15)

    sleep(3)
    tina.clear()
    print("Custom pic challenge")

def mickey():
    base_x = -300
    base_y = -300

    color_list = ["blue", "pink", "purple", "black", "yellow", "green", "red"]

    prev_color = ""

    for _ in range(0, 4):
        base_x = -300
        for _ in range(0, 4):
            random.shuffle(color_list)
            color = color_list[random.randint(0, len(color_list)-1)]
            while (prev_color == color):
                color = color_list[random.randint(0, len(color_list)-1)]
            prev_color = color
            draw_mickey(tina, color, color, base_x, base_y)
            base_x += 180
        base_y += 180
    
    sleep(5) #Wait 5 seconds to admire the beauty
    tina.clear()

while True:
    os.system("cls") #Clear screen (only works with windows)

    print("1. Challenge 3")
    print("2. Challenge 4")
    print("3. Mickey")
    print("0. Exit\n")

    choice = input("Please select a choice: ")

    choice = choice.lower().strip()

    if choice == "1":
        challenge3()
    elif choice == "2":
        challenge4()
    elif choice == "3":
        mickey()
    elif choice == "0":
        exit()
    else:
        input("Incorrect option selected...")