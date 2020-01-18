#!/bin/python

## A = chr(97)
## Z = chr(122)

def EncryptText(text: str, key: int) -> str: ##Function to encrypt text
    newText: str = "" ##Instantiate new text variable

    for char in text: ##Loop through characters in the text
        if char != " ":
            newChr = ord(char) + key ##Add the key to the ord of the char
            while True: ##Loop till newChr is below 122
                if newChr > 122: ##Loop new chr back to 97 if it's above 122
                    newChr = 97 + abs(newChr-122)
                else: ##If it's below 122 then end the loop
                    break
            
            newText += chr(newChr) ##Add new char to new text
        else:
            newText += char ##Ensure spaces aren't tampered with

    return newText ##Return new text



message: str = input("Please input a message to be encrypted: ") ##Get the message the user wants to encrypt
key: int = 0 ##Instantiate key variable

while True: ##User choose key loop
    try: ##Try to convert user input to int
        key = int(input("Please enter a key (E.G 3): "))
    except ValueError: ##Look for value error if the user didn't input a number
        input("\nPlease input a number for the Key!\nPlease hit ENTER/RETURN to try again...")
        continue
    except: ##Something went very wrong if the code got here
        input("\nSomething has gone very wrong!\nPlease hit ENTER/RETURN to try again...")
        continue
    break


print(f"Original Message: {message}")
print(f"Encrypted Message: {EncryptText(message.lower(), key)}")