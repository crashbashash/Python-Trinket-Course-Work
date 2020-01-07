try:
    num1 = float(input("What is your first number?: ").strip().lower())
    num2 = float(input("What is your second number?: ").strip().lower())
    operator = input("What operator will you use?(E.G, \'+\' = Add): ").strip().lower()

    if operator == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif operator == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    elif operator == "*":
        print(f"{num1} * {num2} = {num1*num2}")
    elif operator == "/":
        print(f"{num1} / {num2} = {num1/num2}")
except Exception as e:
    print("Fatal error encountered!!!")
    print(f"Error: {e}")