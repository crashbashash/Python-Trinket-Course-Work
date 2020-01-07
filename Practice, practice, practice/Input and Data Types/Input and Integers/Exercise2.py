try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    print(f"The total of the numbers is {num1+num2+num3}\n"+
      f"The average of the numbers is {round((num1+num2+num3)/3, 2)}\n"+
      f"The product of the numbers is {(num1*num2)*num3}")

except Exception as e:
    print("Failed to run program!!!\n"+
          f"Error: {e}")
