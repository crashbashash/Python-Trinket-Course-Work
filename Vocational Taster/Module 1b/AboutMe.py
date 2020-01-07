#!/bin/python3

print('Hello')

###Print Dog###
print('''
Here\'s a picture of a dog:
 o____
  ||||
''')

###Print Fav Language###
print('''
I like C#
     ####           #   #
   ###          ###########
  ##              #   #
  ##             #   #
   ###       ############
     ####      #   # 
''')

###Print Home Town###
print(''' 
I live in Gillingham
         /\\
        /  \\
       /    \\
      /      \\
     /________\\
     |       #|
     |        |
     |        |
     |    _   |
     |#__|_|__|    
''')

##Start born question loop
while True:
  try: ## Try to parse the answer as an int
    born = int(input("What year were you born?: ")) ##Get the users birth year
    print(f"\nIn the year 2025 you'll be {2025-born} years old!!!")
    input("\nHit ENTER/RETURN to continue...")

    age = int(input("\nWhat is your age?: ")) ##Get the users age
    print(f"\nIf you were a dog, you'd be {age*7}!!")
    print('''
o____
 ||||
    ''')
    input("\nHit ENTER/RETURN to continue...")

    print('Here is some odd pattern')
    print(f'{"x-"*10}\n{"-o"*10}')

    input("\nHit ENTER/RETURN to continue...")

    break
  except Exception as e: ##Detect if the user gives a non number
    print("Incorrect input given, hit ENTER/RETURN to continue...")
    input()
