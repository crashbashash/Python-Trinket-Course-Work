total = 0 ##Store the total of the numbers inputted
inputs = 0 ##Store the total number of inputs processed

while True: ##Start a loop to wait for the correct value to be inputted
    try: ##Use a try statement incase the user inputs something other than a number
        choice = (int)(input('Please choose a number: ')) ##Store the number chosen by the user

        if choice == -1: ##Check if the number is -1
            break ##End the loop if the user guessed correctly

        total += choice ##Add the users choice to the total
        inputs += 1 ##Increment the total number of inputs processed by 1
    except Exception as e: ##Exception statement for when the user inputs something other than a number
        print(f'Invalid input detected, please enter a number...\nError {e}\n\n') ##Tell the user to input a number instead of letters or symbols

print(f'\nThe total is: {total} and the average is {total/inputs}') ##Tell the user the total of the numbers entered and the average of them