from time import sleep #Import sleep from the time module to allow us to pause the program for a period of time
import sys #Import sys to write directly to standard output

def print_word(word, msPerChar): #Function to print a word, character by character
    for char in word: #For loop to iterate through the characters in the word we are priniting to stdout
        sys.stdout.write(char) #Call the stdout write function and write the current character to the terminal
        sleep(msPerChar/1000) #Convert ms to seconds and wait that long before writing another character

print_word("Hello, World!\n", 50) #Print "Hello, World!" and wait 50ms between writing each character

print_word("You have to admit this is pretty sick :D\n", 100)