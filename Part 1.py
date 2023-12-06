with open("seeds.txt", "r") as file:
    data = file.read()
    seeds, *data_blocks = data.split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

for data_block in data_blocks:
    ranges_list = []
    for line in data_block.splitlines()[1:]:
        ranges_list.append(list(map(int, line.split())))

    new_seeds = []

    for seed in seeds:
        for destination, source, length in ranges_list:
            if seed in range(source, source + length + 1):
                new_seeds.append(seed - source + destination)
                break
        else:
            new_seeds.append(seed)

    seeds = new_seeds

lowest = min(seeds)
print(lowest)