try:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    if num1 > num2:
        print("The first number is greater")
    elif num2 > num1:
        print("The second number is greater")
    else:
        print("Both numbers are the same value")
except Exception as e:
    print("Fatal error encountered!!!")
    print(f"Error: {e}")