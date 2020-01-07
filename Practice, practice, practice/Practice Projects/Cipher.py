def Cipher(key = 5, msg = "This is encrypted text"): ##Function to create a cipher
    newMsg = '' ##Create the newMsg variable
    for letter in msg: ##Iterate through the characters in the msg
        if ord(letter) >= 97 and ord(letter) <= 122: ##Check if the msg is a space
            nextLetter = ord(chr(ord(letter)+key)) ##Set the next letter to the current letter plus the key
            while nextLetter > 122: ##Loop while the nextLetter is larger than the max letter
                nextLetter = 97 + (nextLetter - 123) #Set next letter to the lowest letter plus the remainder
            newMsg += chr(nextLetter) #Add the nextLetter to the newMsg
        else:
            newMsg += letter ##Set the usrs message to a space
    
    return newMsg ##Return the new message


usrMsg = input('Please enter a message to encrypt: ') ##Get the message the user wishes to cipher

try:
    usrKey = (int)(input('\nPlease enter a key to use: ')) ##Convert the users key choice to an int
except Exception as e: ##Check if the user throws an error by entering a letter instead of number
    print("Incorrect value given for the key") ##Tell the user the error and quit the application
    print(f"Error: {e}")
    quit()

print(f'Encrypted text: {Cipher(key=usrKey, msg=usrMsg)}') ##Print the users encrypted text