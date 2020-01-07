while True: ##Start the programs main loop
    num1 = 0 ##Create the num1 variable
    num2 = 0 ##Create the num2 variable

    try:
        num1 = (int)(input('\n\nPlease enter the first number: ')) ##Set num1 to be equal to the input of the user and convert it to an integer
        num2 = (int)(input('\nPlease enter the seconds number: ')) ##Set num2 to be equal to the input of the user and convert it to an integer
    except Exception as e: ##Detect if the user hasn't entered a number
        print(f'Invalid input detected, please enter a number next time...\nError: {e}\n') ##Tell the user to try again and display the error for debugging purposes
        input('Hit ENTER/RETURN to continue...') ##Wait for the user to progress to the start of the loop again
        continue ##Go back to the start of the main loop to get the user to try again

    operator = input('\n\nPlease enter an operator to use: ').strip() ##Get the users choice of operator

    if operator == '+': ##Check if the user wishes to add the numbers
        print(f'\n{num1} + {num2} = {num1+num2}\n')
    elif operator == '-': ##Check if the user wishes to subtract the numbers
        print(f'\n{num1} - {num2} = {num1-num2}\n')
    elif operator == '/': ##Check if the user wishes to divide the numbers
        print(f'\n{num1} / {num2} = {num1/num2}\n')
    elif operator == '*': ##Check if the user wished to multiply the numbers
        print(f'\n{num1} * {num2} = {num1*num2}')
    else: ##Check if input is incorrect
        print("\nIncorrect operator given\n")
        input('Hit ENTER/RETURN to try again...')
        continue
    
    tryAgainLoop = True ##Create the try again loop variable and set it to True
    
    while tryAgainLoop: ##Loop till the user makes a selection
        tryAgain = input('\nDo you wish to try again?(y/n): ').strip().lower() ##Get the users choice and format it

        if tryAgain == 'y': ##Start the main loop again if the user selects 'y'
            tryAgainLoop = False
        elif tryAgain == 'n': ##Stop the program if the user selects 'n'
            quit()
        else: ##Continue the try again loop if the user inputs the wrong string
            print('\nIncorrect option given\n')
            input('\nHit ENTER/RETURN to try again....')
    