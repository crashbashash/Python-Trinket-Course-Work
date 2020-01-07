from turtle import Turtle ##Import turtle for graphics stuff
from time import sleep ##Import sleep to wait for x seconds


turtle1 = Turtle(visible=False, shape='turtle') ##Create the first turtle
turtle2 = Turtle(visible=False, shape='turtle') ##Create the second turtle

##Lift both pens up
turtle1.penup()
turtle2.penup()

##Move both turtles
turtle1.goto(-50, 50)
turtle1.goto(50, -50)

##Orient both turtles
turtle1.setheading(180)
turtle2.setheading(0)

##Show both turtles
turtle1.st()
turtle2.st()


stageCount = 0 ##Create the stageCount variable
while True: ##Loop till the convo ends
    if stageCount == 0: ##Stage 0 of the conversation
        turtle1.write("Hey hows it going dude?", align='center')
        sleep(3)
        turtle2.write("Yeah I'm pretty good dude, how's you?", align='center')
        sleep(5)
    elif stageCount == 1: ##Stage 1 of the convo
        turtle1.write("Yeah I'm pretty good bro. Is your fridge running?", align='center')
        sleep(3)
        turtle2.write("Yeah... I should hope so dude", align='center')
        sleep(5)
    elif stageCount == 2: ##Stage 2 of the convo
        turtle1.write("Then you had better go catch it then!", align='center')
        sleep(6)
        turtle2.write("...", align='center')
        sleep(5)
    elif stageCount == 3: ##Stage 3 of the convo
        turtle2.write("Ugh. Get the hell out of here jim", align='center')
        sleep(2)
        turtle1.write(":(", align='center')
        sleep(10)
        break

    ##Clear both turtles dialogue after they have finished a stage
    turtle1.clear()
    turtle2.clear()
    stageCount += 1 ##Increment the stage count by 1 once a stage has completed