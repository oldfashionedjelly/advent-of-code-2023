file_path = 'calibration.txt'
total = 0

with open(file_path, 'r') as file:
    for line in file:
        integers = []
        for i in range(len(line)):
            if line[i].isdigit():
                integers.append(line[i])
        result = integers[0] + integers[-1]
        total+=int(result)

print(total)