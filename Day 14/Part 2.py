from collections import defaultdict

lines = open("rocks.txt").read().split("\n")
(n, m) = (len(lines), len(lines[0]))
pebbles = []
order = []

def rot90(ppos):
    return [(x, n - y - 1) for (y, x) in ppos]

def groupbyx(ppos):
    work = []
    for x in range(m):
        work.append([])
    for y, x in ppos:
        work[x].append(y)
    return work

def parse():
    tmp = []
    pebbles.clear()
    order.clear()
    for y in range(n):
        l = [0] * m
        for x in range(m):
            if lines[y][x] == "O":
                pebbles.append((y, x))
            if lines[y][x] == "#":
                tmp.append((y, x))
    for i in range(4):
        grp = groupbyx(tmp)
        order.append(grp)
        tmp = []
        for x in range(m):
            tmp.extend([(y, x) for y in grp[x]])
        tmp = rot90(tmp)
    return len(pebbles)


def tilt(ppos, rgrp):
    work = groupbyx(ppos)
    next = []
    for x in range(m):
        ofs = 0
        wp = rp = 0
        while wp < len(work[x]) and rp < len(rgrp[x]):
            rocky = rgrp[x][rp]
            pebby = work[x][wp]
            if rocky < pebby:
                ofs = rocky + 1
                rp += 1
            else:  
                next.append((ofs, x))
                ofs += 1
                wp += 1
        while wp < len(work[x]):
            next.append((ofs, x))
            ofs += 1
            wp += 1
    return next

def display(ppos, amap):
    print(ppos)
    for y in range(n):
        for x in range(m):
            if y in amap[x]:
                print("#", end="")
            elif (y, x) in ppos:
                print("O", end="")
            else:
                print(".", end="")
        print()

def load(ppos):
    return sum([n - y for (y, _) in ppos])

def part1():
    return load(tilt(pebbles, order[0]))

def sign(ppos):
    ret = ""
    for x, y in ppos:
        ret += chr(x + 20)
        ret += chr(y + 20)
    return ret


parse()

cache = {}
vals = []
ppos = pebbles
sgn = sign(ppos)
while sgn not in cache:
    cache[sgn] = len(cache)
    vals.append(load(ppos))
    for amap in order:
        ppos = rot90(tilt(ppos, amap))
    sgn = sign(ppos)
cycle_length = len(cache) - cache[sgn]
remaining = (1000000000 - len(cache)) % cycle_length

print(vals[cache[sgn] + remaining])