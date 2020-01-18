#!/bin/python3

import os ##Import os to send cmd commands
from operator import itemgetter ##Import item getter to sort dicts by specific items
from typing import List, Dict ##Import typing for type hinting stuff

def ClearScreen(): ##Clear screen function
    os.system("cls" if os.name == "nt" else "clear")


print("Ashleys super awesome name calculator thingy: \n")

personsList: List[dict] = [] ##Instantiate a list containing info on people the user inputs

while True: ##Main program loop
    while True: ##Main loop to add names
        ##Instantiate the person dictionary
        person: Dict = {
            'name':'',
            'age':0,
            'height':0.0
        }

        name: str = input("\nPlease enter a name (Type STOP to finish adding people): ").replace(" ", "").capitalize() ##Get the name from the user

        if name == "Stop": ##Check if the user wants to stop
            break
        
        age: int = 0 ##Instantiate age variable
        while True: ##Loop to get age input from user
            try: ##Try to convert the users input to an int
                age = int(input("\nPlease enter an age: ").replace(" ", "")) ##Get the age from the user
                break
            except ValueError: ##Check for a value error when converting to an int
                input("\nYou must use a number for the age!!!\nHit ENTER/RETURN to try again...")
                continue
            except: ##Check for some other error
                input("\nSomething went very wrong!!!\nHit ENTER/RETURN to try again...")
                continue

        
        height: float = 0.0 ##Instantiate height variable
        while True: ##Loop to get the height from the user
            try: ##Try to convert the height input to a float
                height = float(input("\nPlease enter a height(Height is in feet, E.G 5.5): ")) ##Get the height from the user
                break
            except ValueError: ##Check for a value error when converting to a float
                input("\nPlease enter a number for the height!!!\nHit ENTER/RETURN to try again...")
                continue
            except: ##Check for some other error
                input("\nSomething went very wrong!!!\nHit ENTER/RETURN to try again...")
                continue
        
        ##Print details of the person the user added
        print(
        f"""
        Name: {name}
        Age: {age}
        Height: {height}
        """
        )

        choice = input("\nDo you want to save this information?(Y/N): ").replace(" ", "").capitalize()

        while True:
            if choice == "Y": ##Check if user wants to save the person
                ##Add user data to the person dictionary
                person['name'] = name
                person['age'] = age
                person['height'] = height

                personsList.append(person) ##Append the persion dict to the persons list
                break
            elif choice == "N": ##Check if the user doesn't wish to input this person into the list
                break
            else: ##Check if the user has inputted an invalid option
                input("\nPlease input either 'Y' or 'N'!!!\nPlease hit ENTER/RETURN to continue...")
                continue

    if len(personsList) > 1: ##Check if the user has inputted more than 1 person into the list
        personsList.sort(key=itemgetter("height")) ##Sort the main list by height
        personsListAgeSort = personsList ##Set the age list to the persons list
        personsListAgeSort.sort(key=itemgetter("age")) ##Sort this list by age

        oldestPerson: str = personsListAgeSort[-1]['name'] ##Set oldest person variable
        oldestAge: int = personsListAgeSort[-1]['age'] ##Set oldest age variable

        youngestPerson: str = personsListAgeSort[0]['name'] ##Set youngest person variable
        youngestAge: int = personsListAgeSort[0]['age'] ##Set youngest age variable

        tallestPerson: str = personsList[-1]['name'] ##Set tallest person variable
        tallestValue: int = personsList[-1]['height'] ##Set tallest value variable

        shortestPerson: str = personsList[0]['name'] ##Set shortest person variable
        shortestValue: int = personsList[0]['height'] ##Set shortest value variable

        ##Print information about the people in the persons list
        print(
        f"""
        {oldestPerson} is the oldest person at {oldestAge}
        {youngestPerson} is the youngest person at {youngestAge}
        {tallestPerson} is the tallest person at {tallestValue}
        {shortestPerson} is the shortest person at {shortestValue}
        """
        )
        break
    else: ##If not get them to enter more people into the list
        input("\nPlease enter more than 1 person in the list!!!\nHit ENTER/RETURN to continue...")
        continue ##Continue the main loop to get the user to input more people into the list
