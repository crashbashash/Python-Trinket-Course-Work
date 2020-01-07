num_list = "["

for i in range (500, 1500):
    if i % 3 == 0:
        if i % 10 == 0:
            num_list += str(i) + ", "
num_list = num_list.strip()[ : -1] + "]"

print(num_list)