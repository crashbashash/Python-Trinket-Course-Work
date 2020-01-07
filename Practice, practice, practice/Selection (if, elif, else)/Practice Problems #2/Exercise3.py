try:
    money = float(input("How much money have you got?(£): "))

    if money < 250:
        print("You cannot afford to buy anything")
    elif money >= 250 and money < 450:
        print("You can afford to buy a tablet")
    elif money >= 450 and money < 500:
        print("You can addord to buy a PC")
    elif money >= 500 and money <= 700:
        print("You can afford to buy a Mac")
    elif money > 700 and money <= 1000:
        print("You can afford to buy a tablet and a PC")
    else:
        print("You are a very lucky person")
except Exception as e:
    print("Fatal error encountered!!!")
    print(f"Error: {e}")