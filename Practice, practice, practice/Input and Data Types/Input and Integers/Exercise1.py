first_name = input("Please enter your first name: ")
age = input("\nPlease enter your age: ")

try:
    print(f"\nHi {first_name.capitalize()} in 5 years you will be {int(age)+5}")
except Exception as e:
    print("\nFailed to finish program!!!\n"+
          f"Error: {e}")
