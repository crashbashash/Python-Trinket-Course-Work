#!/bin/python3

from random import randint ##Import randint for random whole numbers
import os ##Import os to clear the terminal screen

def ClearScreen(): ##Clear screen function
    os.system('cls' if os.name == 'nt' else 'clear')

while True: ##Main Program loop
    rNum: int = randint(1,50) ##Generate a random number
    uNum = "" ##Instantiate the user number variable
    attempts: int = 0 ##Instantiate the attempts variable
    numsTried = [] ##Tried number list

    ClearScreen()
    print("The program has selected a random number between 1 and 50.\n"+
        "It is your job to figure out what that number is, in 6 attempts.")
    while True: ##Game loop
        try: ##Try to convert user input to an int
            uNum = input("\nWhat number do you think it is (Q = Quit)?: ").replace(" ", "")
            uNum = int(uNum)
        except: ##If it fails the user has inputted something other than a number
            if str(uNum).capitalize() == "Q":
                quit()
            input("\nPlease only input numbers!!!\n"+
            "HIT ENTER/RETURN to continue...")
            continue ##Restart the game loop
        
        if uNum < 1 or uNum > 50: ##Check if the users number is out of the bounds of that random number
            input("\nThe number you chose is not between 1 and 50!\n"+
            "Hit ENTER/RETURN to try again...")
            continue ##Restart the game loop

        if uNum not in numsTried: ##Check if the users guessed number is not in the list of numbers they have tried
            numsTried.append(uNum)
        else: ##Restart the loop if the number is in the list of tried numbers
            input("\nPlease do not input numbers you have already tried.\nPlease hit ENTER/RETURN to continue...")
            continue
        
        if uNum == rNum: ##Check if the user guesses correctly
            if input(f"\nCongratulations you have guessed the correct number {rNum}\nTo quit enter Q, to continue just hit ENTER/RETURN: ").replace(" ", "").capitalize()[0] == "Q": ##Check if the user wishes to quit
                quit() ##Quit the program
            else:
                break ##Restart the game
        
        if attempts >= 6: ##Check if the user has used all their attempts
            input("\nYou have failed to guess the correct number!\nHit ENTER/RETURN to continue...")
            break
        else: ##If not then increment attempts by 1
            print("Incorrect number!!!\n")
            attempts += 1