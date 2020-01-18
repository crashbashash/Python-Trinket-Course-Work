#!/bin/python3

from random import shuffle ##Import shuffle from random to shuffle and randomise lists

rainbow = ["red", "yellow", "pink", "green", "orange", "purple", "blue"] ##Rainbow list
shuffle(rainbow) ##Shuffle the rainbow color list

for i, color in enumerate(rainbow, start=1): ##Rainbow color loop
    pos = "" ##Instantiate name of position variable
    ##Use if statement to determine what the position should be called
    if i == 1:
        pos = "1st"
    elif i == 2:
        pos = "2nd"
    elif i == 3:
        pos = "3rd"
    else:
        pos = f"{i}th"
    
    print(f"\nThe {pos} colour in the rainbow is: {color}") ##Print the position of the color and what color it is
