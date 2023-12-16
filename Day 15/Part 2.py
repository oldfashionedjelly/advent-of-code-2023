codes = open("codes.txt").read().split(",")

boxes = [{"labels":[], "lengths":[]} for i in range(256)]

for code in codes:
    label = code[:-1] if "-" in code else code[:-2]
    rest = code[len(label):]
    box = 0
    for char in label:
        box += ord(char)
        box *= 17
        box %= 256
    if rest == "-":
        if label in boxes[box]["labels"]:
            i = boxes[box]["labels"].index(label)
            boxes[box]["labels"].pop(i)
            boxes[box]["lengths"].pop(i)
    elif label in boxes[box]["labels"]:
        i = boxes[box]["labels"].index(label)
        boxes[box]["lengths"][i] = int(rest[-1])
    else:
        boxes[box]["labels"].append(label)
        boxes[box]["lengths"].append(int(rest[-1]))

print(sum(
    (i+1)*(j+1)*(boxes[i]["lengths"][j])
    for i in range(len(boxes))
    for j in range(len(boxes[i]["labels"]))
))