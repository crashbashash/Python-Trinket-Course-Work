def GenNums(num = 3, valueToReach = 20000): ##Function to increment a number till it reaches a desired value
    curNum = num ##Set cur num to num
    while curNum < valueToReach: ##Stay in a loop until curNum becomes greater than the desired value
        print(f'{curNum} ', end='') ##Print the current number to the screen
        curNum *= num ##Times the curNum by the number the user inputted


try: ##Encapsulate the input in a try statement incase the user inputs something other than a number
    choice = (int)(input("Please choose a number: ")) ##Get the users choice of number and convert it to an int
    print("\n")
    GenNums(num=choice) ##Generate some numbers till it reaches a desired value
except Exception as e: ##Exception statement gets used for when the user inputs something other than a number
    print(f'Invalid option selected, please input a number...\nError: {e}') ##Tell the user to correct their mistake and what the error is for debugging purposes

