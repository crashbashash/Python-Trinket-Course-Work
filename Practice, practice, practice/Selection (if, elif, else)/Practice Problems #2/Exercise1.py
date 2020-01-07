try:
    temp = int(input("What is the current temperature?: "))

    if temp <= 16:
        print("Put on a coat")
    elif temp >= 17 and temp <= 19:
        print("Wear a long-sleeved top")
    else:
        print("Wear a t-shirt")
except Exception as e:
    print("Fatal error encountered!!!")
    print(f"Error: {e}")