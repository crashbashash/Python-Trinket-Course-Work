try:
    with open("dimensions.txt") as dimension_file:
        height, width, depth = dimension_file.readline().replace(" ", "").split(",")
    
    print(f"{str(((float(width)/8)*(float(depth)/8))*(float(height)/11)).split('.')[0]} tins can fit in this box")
except Exception as e:
    print("Fatal error encountered!!!\n"+
          f"Error: {e}")
