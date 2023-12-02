file_path = 'results.txt'
global total
total=0

def is_input_possible(input_str):
    game, games=input_str.split(': ')
    input_list = games.split(', ')
    blue=0
    red=0
    green=0
    for item in input_list:
        count, color = item.split()
        count = int(count)
        if color == "blue":
            blue+=count
        if color == "green":
            green+=count 
        if color == "red":
            red+=count

        if blue>14 or red>12 or green>13:
            return False
        else:
            return True

def getGame(line):
    game, games=line.split(': ')
    game, num=game.split(' ')
    return int(num)

with open(file_path, 'r') as file:
    for line in file:
        result = is_input_possible(line)
        if result:
            total+=getGame(line)
        print(result)


print(total)