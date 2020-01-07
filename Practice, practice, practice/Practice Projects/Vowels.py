def CountVowels(message): ##Function to count vowels in message
    vowels =  ['a','e','i','o','u'] #List of vowelz
    vowelCount = 0 #Create a vowelcount variable to keep track of the vowels found

    for letter in message: ##Iterate through the letters in the message
        for vowel in vowels:  ##Iterate through the vowels in the vowel list
            if letter == vowel: ##Check if the current letter is a vowel
                vowelCount += 1 ##Increment the vowel count by 1
                break #Break out of this for loop
    return vowelCount #Return the vowel count


msg = input("Please enter a message: ").replace(" ", "").lower() ##Get the users message and format it

print(f'That message has {CountVowels(msg)} vowels!!!') ##Print how many vowels the message contained to the user