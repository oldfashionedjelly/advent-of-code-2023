file_path = 'calibration.txt'
total = 0
words =["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbesr = [1,2,3,4,5,6,7,8,9]

with open(file_path, 'r') as file:
    for line in file:
        integers = []
        for i in range(len(line)):
            if line[i].isdigit():
                integers.append(line[i])
        result = integers[0] + integers[-1]
        total+=int(result)

print(total)