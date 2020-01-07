try:
    number = int(input("Enter a number to see its times table: "))
    
    print(f"{number} times table: \n")
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")
except Exception as e:
    print("Fatal error encountered!!!")
    print(f"Error: {e}")