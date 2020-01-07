from random import randint ##Import randint for some random fun

def GenCorrectNum(minValue = 1, maxValue = 100, correctValue = 1): ##Function to generate random numbers in an attemp to generate the correct number
    print(f'Correct value to generate = {correctValue}\n')
    attempts = 0 ##Store how many attempts it takes to complete
    total = 0 ##Store the total of the numbers generated
    while True: ##Start a loop to generate the correct number
        attempts += 1 ##Increment the attempts variable by 1
        num = randint(minValue, maxValue) ##Set the num variable to a random value between the minValue and maxValue variable
        total += num ##Add the generated number to the total number variable
        print(f'{attempts}: {num}') ##Print the attempt number and the number generated to the screen
        if num == correctValue: ##Check if the generated number is equal to the number we are trying to generate
            print(f'\nThe value {correctValue} has been found in {attempts} attempts!!!') ##Tell the user the correct value has been found and how many attempts it took
            print(f'The total of the generated numbers is {total}') ##Tell the user the total of the generated numbers
            break ##Break out of the loop because we have found the correct value


GenCorrectNum() ##Generate random numbers to try and find a speicified value