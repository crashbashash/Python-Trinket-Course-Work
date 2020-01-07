print(f"The volume of a tin of beans is {bean_volume}, how many can fit in your box?\n")

try:
    height = float(input("Enter the height of the box: "))
    width = float(input("Enter the width of the box: "))
    depth = float(input("Enter the depth of the box: "))

    print(f"{str(((float(width)/8)*(float(depth)/8))*(float(height)/11)).split('.')[0]} tins can fit in this box")
except Exception as e:
    print("Failed to finish the program!!!\n"+
          f"Error: {e}")

