inp = open('pipes.txt').read().split()

width = len(inp[0])
height = len(inp)

data = ''.join(inp)

dmap = {
    'S': [],
    '|': [width, -width],
    '-': [-1, 1],
    '.': [],
    '7': [-1, width],
    'L': [1, -width],
    'J': [-1, -width],
    'F': [1, width]
}

start = data.find('S')
path = {start}
data = [dmap[c] for c in data]

for i, offsets in enumerate(data):
    if start in (i + o for o in offsets):
        dmap['S'].append(i - start)

dist = 0
new = None
while 1:
    new2 = new
    new = set()
    for p in (new2 or path):
        for offset in data[p]:
            if p + offset not in path:
                new.add(p + offset)
    
    if new:
        path |= new
        dist += 1
    else:
        break

inside = 0
for i in range(len(data)):
    if i in path:
        continue
    outside_right = outside_left = True
    j = i
    while j > 0:
        if j in path and 1 in data[j]:
            outside_right = not outside_right
        if j in path and -1 in data[j]:
            outside_left = not outside_left
        j -= width

    if not (outside_right or outside_left):
        inside += 1

print(inside)
