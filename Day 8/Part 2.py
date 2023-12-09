from math import lcm

class Game:
    def __init__(self, rules):
        self.D = {}
        self.F = set()
        self.S = []
        for id, l in enumerate(rules):
            n = l[0:3]
            self.D[n] = id
            if n[-1] == "A":
                self.S.append(id)
            if n[-1] == "Z":
                self.F.add(id)
        self.L = [-1] * len(self.D)
        self.R = [-1] * len(self.D)
        for l in lines[2:]:
            n = self.D[l[0:3]]
            self.L[n] = self.D[l[7:10]]
            self.R[n] = self.D[l[12:15]]


lines = open("route.txt").read().split("\n")
g = Game(lines[2:])
ins = lines[0]

z = 1
m = len(ins)
for start in g.S:
    s = 0
    id = start
    while id not in g.F:
        c = ins[s % m]
        if c == "L":
            id = g.L[id]
        else:
            id = g.R[id]
        s = s + 1
    z = lcm(z, s)
print(z)