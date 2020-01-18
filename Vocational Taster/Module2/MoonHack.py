 #!/bin/python3

import os

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
 
##Items for the mission
items = [
"A: 3 litres of water",
"B: Shampoo",
"C: An extra Spacesuit",
"D: A shovel",
"E: A 10 day oxygen supply",
"F: Solar panels",
"G: The seeds for your mission",
"H: The soil for your mission",
"I: A 3 day food supply",
"J: Bacon",
"K: Single slice of cheese",
"L: Crisps"
]

##Main program loop
while True:
    ClearScreen() ##Clear the screen if using a terminal

    ##Print the breifing
    print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
    print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
    print("You can get to the base in 3 days on your lunar rover")
    print("The lunar rover can only fit you in your spacesuit and 4 other items")
    print("Out of the items below, which do you bring? \n")


    print("Type the letter of the 4 items you would like to bring seperated by commas.\n Ex: A, B, C, D") ##Tell the user what to do

    ##Show the items to the user
    for item in items:
        print(item)

    choice = input("\nWhat 4 items would you like to take with you?: ").replace(" ", "").split(',') ##Get and format the users choice

    ##Check if the user didn't input 4 items
    if len(choice) != 4:
        print("You must take 4 items with you!!!")
        input("\nHit ENTER/RETURN to continue...")
        continue #Restart the main loop

    ##If statements to give feedback to the player based on the items they chose
    if "A" not in choice:
        print("Without water every day, you will dehydrate!!!")
    
    if "E" not in choice:
        print("Without oxygen you will not be able to breath!")

    if "F" not in choice:
        print("Without solar panels, your lunar rover will not make it to the base")

    if "I" not in choice:
        print("You will surely starve if you take no food with you")

    if "K" in choice:
        print("You will not get far with a single slice of cheese...")
    
    ##Check if the player has selected the correct items
    if "A" in choice and "E" in choice and "F" in choice and "I" in choice:
        print("\nCongratz you will make it too the moonbase alive!!!")
    else:
        print("\nYou have failed to select the correct items")
        input("\nPlease hit ENTER/RETURN to continue")
        continue ##If the user fails to select the correct items then restart the loop

    break ##Break out of the main loop if the user guesses the items correctly