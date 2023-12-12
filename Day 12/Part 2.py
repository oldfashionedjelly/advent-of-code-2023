from functools import cache

@cache
def calc(record, groups):
    if len(groups) == 0: 
        return 1 if '#' not in record else 0
    if sum(groups) + len(groups) - 1 > len(record): 
        return 0

    if record[0] == '.': 
        return calc(record[1:], groups)

    num = 0
    if record[0] == '?': 
        num += calc(record[1:], groups) 

    if '.' not in record[:groups[0]] and (len(record) <= groups[0] or len(record) > groups[0] and record[groups[0]] != '#'):
            num += calc(record[groups[0]+1:], groups[1:])

    return num

total = 0
with open('springs.txt', 'r') as f:
    for line in f.read().splitlines():
        record, groups = line.split(' ')
        record = (5*(record + '?'))[:-1] 
        groups = 5*[int(x) for x in groups.split(',')]
        total += calc(tuple(record), tuple(groups))

print(total) 