while True: ##Create a loop for the program
    num = 0 ##Create the num variable
    try: ##Use a try statement incase the user inputs something other than a number
        num = (int)(input("Choose a number between 1-10: ")) ##Get the users number choice and convert it to an int
    except Exception as e: ##Exception statement incase the user inputs a letter or symbol
        print(f'\nInvalid input detected!!!\nError: {e}\n\n\n') ##Tell the user they have messed up
        continue ##Start the loop over again

    if not (num >= 1 and num <= 10): ##Check if the number chosen isn't between 1 and 10
        print("\nInvalid input!\n\n\n") ##Tell the user they have failed to input the correct value
        continue ##Start the loop over again
    
    print("\nValid input, well done") ##Tell the user they have inputted the correct number
    break ##End the loop because the user has passed all the other checks and has inputted the correct number

