try:
    number = int(input("Please enter a positive/negative number here: "))

    if number < 0:
        print(f"\n{number} is a negative number")
    else:
        print(f"\n{number} is a positive number")
except Exception as e:
    print("Fatal Error Encountered!!!")
    print(f"Error: {e}")