#!/bin/python3
from random import randint ##Import randint for bot choice
from typing import List ##Import List typing for type hinting

allChoices: List[str] = ['Rock-Scissors', 'Paper-Rock', 'Scissors-Paper'] #All Available choices


def GetBotChoice(): ##Get the bot choice
    return allChoices[randint(0, len(allChoices)-1)]


def GetPlayerChoice(choice: int): ##Get the players choice
    if choice > len(allChoices) or choice <= 0:
        return False
    else:
        return allChoices[choice-1]


def ListChoices(): ##List all choices available to the player
    for i, choice in enumerate(allChoices, start=1):
        print(f"{i}. {choice.split('-')[0]}\n")


def GetPlayerWin(pChoiceRaw: str, bChoiceRaw: str): ##See if player has won
    pChoice = pChoiceRaw.split("-")
    bChoice = bChoiceRaw.split("-")

    if pChoice[1] == bChoice[0] and bChoice[1] != pChoice[0]: #Player win
        return "Player Wins"
    elif pChoice[1] != bChoice[0] and bChoice[1] == pChoice[0]: ##Bot win
        return "Bot Wins"
    elif pChoice[0] != bChoice[1] and bChoice[0] != pChoice[1]: #Draw
        return "Draw"
    else: #How you get here?
        return "Something went very wrong!!!"


print("Rock papaer scissors game:\n\n") ##Title of program

ListChoices() ##List all available choices

try: ##Try to convert the players choice to an int
    choice = int(input("\nWhat is your choice: "))
except:
    print("Input is not a number!!!") ##Tell the user they failed
    exit() ##Exit the program



bChoice = GetBotChoice().replace(" ", "")  ##Get bots choice
if not (pChoice := GetPlayerChoice(choice)): ##Get players choice
    print("\nIncorrect choice selected")
    exit()

bcf = bChoice.split('-')[0] ##Store the choice part of bChoice
pcf = pChoice.replace(" ", "").split('-')[0] ##Store the choice part of pChoice

bChoiceIcon = "" ##Instantiate bots choice icon
pChoiceIcon = "" ##Instantiate players choice icon


## Bot choice icon selector
if bcf == "Rock": ##Display icon for rock
    bChoiceIcon = "o"
elif bcf == "Paper": ##Display icon for paper
    bChoiceIcon = "___"
elif bcf == "Scissors": ##Display icon for scissors
    bChoiceIcon = ">8"
else: ##Set icon to the text version of the choice
    bChoiceIcon = bcf

## Player choice icon selector
if pcf == "Rock": ##Display icon for rock
    pChoiceIcon = "o"
elif pcf == "Paper": ##Display icon for paper
    pChoiceIcon = "___"
elif pcf == "Scissors": ##Display icon for scissors
    pChoiceIcon = ">8"
else: ##Set icon to the text version of the choice
    pChoiceIcon = pcf


print(f"\n{pChoiceIcon} vs {bChoiceIcon}\n") ##Display the players and bots choice

print(GetPlayerWin(GetPlayerChoice(choice),bChoice)) ##Display who the winner is
