try:
    num1 = int(input("Please enter the num to count from: "))
    num2 = int(input("Please enter the num to count to: "))

    iter_num = ""
    for i in range(num1, num2+1):
        if i % 2 != 0:
            iter_num += str(i) + " "
    print(iter_num.strip())
except Exception as e:
    print("Fatal error encountered")
    print(f"Error: {e}")