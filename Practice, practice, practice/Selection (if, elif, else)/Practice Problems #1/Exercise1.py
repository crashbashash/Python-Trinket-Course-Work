try:
    age = int(input("What is your age?: "))

    if age < 21:
        print(f"You are {age} you cannot drive in New York")
    else:
        print(f"You are {age} you can drive in New York!!!")
except Exception as e:
    print("Fatal error encountered!!!")
    print(f"Error: {e}")