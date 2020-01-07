from turtle import Turtle #Import turtle for graphics stuff

def DrawTriangle(pen, size = 40, colors = ['blue', 'red', 'purple']):
    pen.setheading(0) #Set heading to east

    for _ in range(3):
        pen.forward(size) ##Move forward by size of triangle
        pen.left(120) ##Move pen left

    pen.ht() #Hide pen when done

pen = Turtle() #Create pen object

DrawTriangle(pen, 40) #Draw triangle

input() #Wait for user to exit the software