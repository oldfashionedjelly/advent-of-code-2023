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

total = 0 

for mirror in pattern:
    old_reflection = find(mirror)
    total += old_reflection
                    
print(total)