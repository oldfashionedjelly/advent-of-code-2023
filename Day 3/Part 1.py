import re

def read_engine_schematic(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def sum_of_part_numbers(engine):
    symbols = {'*', '+', '#', '$', '=', '/', '&', '%', '@', '-'}
    total_sum = 0

    for i in range(len(engine)):
        for j in range(len(engine[i])):
            if engine[i][j] in symbols:
                adjacent_numbers = re.findall(r'\d+', ''.join(engine[i-1:i+2]).ljust(j+2).rjust(j+3))
                valid_numbers = [int(num) for num in adjacent_numbers]
                total_sum += sum(valid_numbers)

    return total_sum

def read_engine_schematic(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

file_path = 'input.txt'
engine_schematic = read_engine_schematic(file_path)

result = sum_of_part_numbers(engine_schematic)
print("Sum of all part numbers:", result)
