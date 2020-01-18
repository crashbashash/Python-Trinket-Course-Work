#!/bin/python3

from typing import List, Dict ##Import typings for List and Dict to be used for type hinting
import os ##Import os to clear the terminal screen

##Create the list of cars the software knows
carList: List[dict] = [
    {
        "make":"Vauxhall",
        "model":"Corsa",
        "engineSize":1199,
        "fuelType":"Unleaded",
        "numDoors":5
    },
    {
        "make":"Ford",
        "model":"Fiesta",
        "engineSize":1299,
        "fuelType":"Unleaded",
        "numDoors":5
    },
    {
        "make":"Fiat",
        "model":"500",
        "engineSize":1099,
        "fuelType":"Unleaded",
        "numDoors":3
    },
    {
        "make":"Ford",
        "model":"Focus",
        "engineSize":1499,
        "fuelType":"Unleaded",
        "numDoors":5
    },
    {
        "make":"Ford",
        "model":"Transit",
        "engineSize":1599,
        "fuelType":"Diesel",
        "numDoors":4
    }
]


def ClearScreen(): ##Clear screen function
    os.system('cls' if os.name == 'nt' else 'clear')


##Function to get the available car makes
def GetCarMakes() -> List[str]:
    makeList: List[str] = []
    for car in carList: ##Iterate through all the cars in the master car list
        if car['make'].capitalize() not in makeList: ##Check if the make is not already in the makes found list
            makeList.append(car['make'].capitalize()) ##Add the new make to the found makes list

    return makeList

while True: ##Main program loop
    ClearScreen() ##Clear the terminal if the user is using one
    print("Car Manufacturers to select from: \n")
    makeList: List[str] = GetCarMakes() ##Get all the makes available to the user

    for i, make in enumerate(makeList, start=1): ##List all the makes available
        print(f"{i}. {make}\n")

    uChoice = input("\nWhat manufacturer do you want to select (E.G Fiat)?: ").capitalize().replace(" ", "") ##Ask the user what make they wish to view

    try: ##Try to convert the users choice to an int to detect if they entered a number instead of letters
        uChoice = int(uChoice) ##Convert users choice to an int
        uChoice = makeList[uChoice-1] ##Convert the number version of the choice to the corresponding make
    except ValueError: ##Check for a value error to see if converting the choice to an int failed
        if uChoice not in makeList:
            input(f"\nWe do not have any cars made by {uChoice}!\nHit ENTER/RETURN to continue...")
            continue
    except: ##Check for other errors when processing the data
        input("\nIncorrect choice selected!\nHit ENTER/RETURN to continue...")
        continue
    
    carsFound = 0 ##Store how many cars have been found that are the same make as the one requested by the user
    for car in carList: ##Loop through available cars
        if car['make'].capitalize() == uChoice.capitalize(): ##Check if the car we are looking at is the same make as the make the user wants to view
            carsFound += 1
            ##Print information about the vehicle
            print(
f"""
Vehicle No.{carsFound} details:

{uChoice} {car['model']} {car['numDoors']} door
Engine Size {car['engineSize']}cc
Fuel {car['fuelType']}
"""
            )

    if input("\nHit ENTER/RETURN to look at other cars or enter 'Q' to quit: ").replace(" ", "").capitalize() == "Q": ##Break out of main loop if the user wishes to Quit
        break ##Break out of the main loop
