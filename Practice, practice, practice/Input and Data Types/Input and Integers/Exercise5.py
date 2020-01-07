import os

runLoc = os.path.dirname(os.path.realpath(__file__))+"/"

try:
    lines = 0

    with open(runLoc+"dimensions.txt") as f:
        for line in iter(lambda: f.readline(), ''):
            lines += 1
    
    boxes = [None] * lines
    with open(runLoc+"dimensions.txt") as file:
        count = 0
        for line in iter(lambda: file.readline(), ''):
            boxes[count] = line.replace(" ", "")
            line = file.readline()
            count += 1

    box_count = 1
    for box in boxes:
        if box != None:
            height, width, depth = box.replace(" ", "").split(",")
            print(f"{str(((float(width)/8)*(float(depth)/8))*(float(height)/11)).split('.')[0]} tins can fit in box {box_count}")
            box_count += 1
except Exception as e:
    print("Fatal error occured!!!\n"+
          f"Error: {e}")
