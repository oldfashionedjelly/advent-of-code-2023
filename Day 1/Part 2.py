import re

file_path = 'calibration.txt'
total = 0
word_to_number = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

with open(file_path, 'r') as file:
    for line in file:
        matches = re.findall(r'\b(?:' + '|'.join(word_to_number.keys()) + r'|\d+)\b', line)
        integers = [word_to_number.get(match, int(match)) for match in matches]
        result = integers[0] + integers[-1]
        total+=int(result)

print(total)