import math

lines = open("races.txt").read().split("\n")

def quadratic(t, d):
    delta = t * t - 4 * d
    if delta <= 0:
        return 0
    x0 = math.ceil((t - math.sqrt(delta)) / 2)
    x1 = math.floor((t + math.sqrt(delta)) / 2)
    if x0 * (t - x0) == d:
        x0 += 1
    if x1 * (t - x1) == d:
        x1 -= 1
    return (x1 - x0) + 1


times = list(map(int, lines[0].split()[1:]))
dist = list(map(int, lines[1].split()[1:]))
s = 1
for i in range(len(times)):
    s *= quadratic(times[i], dist[i])
print(s)