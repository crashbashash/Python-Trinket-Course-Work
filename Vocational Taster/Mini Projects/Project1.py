#!/bin/python3

from typing import List

def IsVowel(char: chr) -> bool: ##Function to see if a character is a vowel
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u'] ##Create list of vowels

    if char.lower() in vowels: ##Check if character is in the vowels list
        return True
    else:
        return False


def GetNumVowels(text: str) -> int: ##Get number of vowels in a string
    numVowels = 0 ##Instantiate number of vowels variable

    for char in text: ##Loop through characters in the text
        if IsVowel(char): ##Check if character is a vowel
            numVowels += 1 ##Increment num of vowels variable

    return numVowels ##Return number of vowels in string


uText: str = input("\nPlease enter a message: ") ##Get the users message

print(f"{uText} ({GetNumVowels(uText)})") ##Print the message and number of vowels in it
