smallestNum = 0 ###Set the smallest number to 0
biggestNum = 0 ##Set the biggest num to 0

firstRun = True ##Create and set the firstRun variable to True

while True: ##Start the loop to check for the num 999 in the users input
    try: ##Try statement to check if an error occurs grabbing the users input
        choice = (int)(input('\n\nPlease input a number: ')) ##Get the num choice of the user and convert it to an int

        if choice == 999: ##Check if the choice is 999
            print(f'\nThe largest number is {biggestNum} and the smallest number is {smallestNum}') ##Tell the user the biggest and smallest number they entered
            break ##Exit the loop when done

        if firstRun: ##Check if this is the first time running the application
            biggestNum = choice ##Set the biggestNum equal to the users number
            smallestNum = choice ##Set the smallest number equal to the users number
            firstRun = False ##Set first run to false to ensure we don't repeat this code again
        else:
            if choice > biggestNum: ##If the choice is bigger than the biggest num then that is the biggest num
                biggestNum = choice
            if choice < smallestNum: ##Pretty much the opposite of the above statement
                smallestNum = choice        
    except Exception as e: ##Catch an error the user might have caused
        print(f'Invalid input detected, please enter a number...\nError {e}') ##Tell the user to enter a number and show the error for debugging purposes