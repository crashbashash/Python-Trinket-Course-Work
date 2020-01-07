while True:
    name = input("Input a name with atleast 5 characters: ")

    if len(name) < 5:
        print("\nYou must input a name with atleast 5 characters to progress\n")
        input("Hit ENTER/RETURN to continue...")
        print("\n"*3)
    else:
        print(f"First letter is {name[0]}, fourth letter is {name[3]}\n")
        break
