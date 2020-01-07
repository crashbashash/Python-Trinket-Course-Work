try:
    number = int(input("Please enter a number: "))

    iter_num = ""
    while number > 0:
        iter_num += str(number) + " "
        number -= 1
    print(iter_num.strip())
except Exception as e:
    print("Fatal error encountered")
    print(f"Error: {e}")