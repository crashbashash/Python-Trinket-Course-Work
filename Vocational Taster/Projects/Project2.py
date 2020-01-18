#!/bin/python3

from random import randint ##Import randint to generate random integers
from typing import List ##Import typing for Lists to be used for type hinting
from math import floor ##Import floor to round the average number down

print("The software will now generate a list of numbers until it is able to generate a positive number...")

numList: List[int] = [] ##Instantiate num list

while True: ##Number generate loop
    num = randint(-10, 100) ##Generate a random number
    numList.append(num) ##Append that number to the list of generated numbers
    
    if num < 0: ##Check if the number is a negative number
        break ##Stop the loop


biggestNum = ""
smallestNum = ""
averageNum = 0
for i, number in enumerate(numList, start=1): ##Loop through the generated numbers to print them
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

    ##Set the biggest and smallest num to the num value if they aren't set yet
    if biggestNum == "" and smallestNum == "":
        biggestNum = number
        smallestNum = number
    else: ##Figure out if the current num is bigger than the biggestnum or small than the smallest num
        if number > biggestNum:
            biggestNum = number
        if number < smallestNum:#
            smallestNum = number

    averageNum += number ##Add the current number to the average

    print(f"The {pos} number is: {number}") ##Show the user a number that was generate by the program


averageNum = averageNum / len(numList) ##Finish calculating the average

print(f"The biggest number generated was: {biggestNum}") ##Print the biggest num
print(f"The smallest number generated was: {smallestNum}") ##print the smallest num
print(f"The average number generated was: {floor(averageNum)}") ##Print the average num