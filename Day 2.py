pattern = [[list(y) for y in x.split("\n")] for x in open("pattern.txt").read().split("\n\n")]

def find(mirror, old_reflection = 0):
    for i in range(1, len(mirror[0])):
        m = min([len(mirror[0][:i]),len(mirror[0][i:])])
        if len(mirror[0][:i]) < len(mirror[0][i:]):
            if [x[:i] for x in mirror] == [x[i:i+m][::-1] for x in mirror]:
                if i != old_reflection:
                    return i
        if len(mirror[0][:i]) > len(mirror[0][i:]):
            if [x[i-m:i] for x in mirror] == [x[i:][::-1] for x in mirror]:
                if i != old_reflection:
                    return i 
    for i in range(1, len(mirror)):
        m = min([len(mirror[:i]),len(mirror[i:])])
        if len(mirror[:i]) < len(mirror[i:]):
            if mirror[:i] == mirror[i:i+m][::-1]:
                if i* 100 != old_reflection:
                    return i * 100
        if len(mirror[:i]) > len(mirror[i:]):
            if mirror[i-m:i] == mirror[i:][::-1]:
                if i* 100 != old_reflection:
                    return i * 100
    return 0

def smudge_removal(mirror, old_reflection):
    for row in range(len(mirror)):
        for col in range(len(mirror[0])):
            if mirror[row][col] == "#":
                mirror[row][col] = "."
                new_reflection = find(mirror, old_reflection = old_reflection)
                if new_reflection != 0:
                    return new_reflection 
                else: 
                    mirror[row][col] = "#"
            if mirror[row][col] == ".":
                mirror[row][col] = "#"
                new_reflection = find(mirror, old_reflection = old_reflection )
                if new_reflection != 0:
                    return new_reflection 
                else: 
                    mirror[row][col] = "."
    return 0

total = 0

for mirror in pattern:
    old_reflection = find(mirror)
    total += smudge_removal(mirror, old_reflection)
                    
print(total)