try:
    number = int(input("Enter a positive/negative number: "))

    if number < 0:
        print(f"{number} is a negative number")
    elif number > 0:
        print(f"{number} is a positive number")
    else:
        print(f"{number} is neither a positive nor a negative")
except Exception as e:
    print("Fatal error encountered")
    print(f"Error: {e}")