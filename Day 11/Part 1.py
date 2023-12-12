filename = "galaxies.txt"

def read_galaxy() -> tuple[list[list[str]], int]:
    galaxy = []
    num_galaxies = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            row = []
            for char in line.strip():
                if char == "#":
                    row.append(num_galaxies)
                    num_galaxies += 1
                else:
                    row.append(char)
            galaxy.append(row)
    return galaxy, num_galaxies


def expand_galaxy(galaxy: list[list[str]]) -> list[list[str]]:
    new_galaxy = []
    for row in galaxy:
        new_galaxy.append(row)
        if all([char == "." for char in row]):
            new_galaxy.append(row)
    
    galaxy = new_galaxy
    new_galaxy = [[] for _ in galaxy]
    for idy in range(len(galaxy[0])):
        for idx in range(len(galaxy)):
            new_galaxy[idx].append(galaxy[idx][idy])
        if all([galaxy[idx][idy] == "." for idx in range(len(galaxy))]):
            for idx in range(len(galaxy)):
                new_galaxy[idx].append(galaxy[idx][idy])
                
    return new_galaxy


def get_galaxies_positions(galaxy: list[list[str]]) -> dict[int, tuple[int, int]]:
    return {
        galaxy[idx][idy]: (idx, idy)
        for idx in range(len(galaxy))
        for idy in range(len(galaxy[0]))
        if galaxy[idx][idy] != "."
    }


def manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return sum([abs(point1[0] - point2[0]), abs(point1[1] - point2[1])])

            
galaxy, num_galaxies = read_galaxy()
galaxy = expand_galaxy(galaxy)
galaxies_positions = {
    galaxy[idx][idy]: (idx, idy)
    for idx in range(len(galaxy))
    for idy in range(len(galaxy[0]))
    if galaxy[idx][idy] != "."
}
pairs = [(i, j) for i in range(num_galaxies) for j in range(i, num_galaxies) if i < j]
total = sum([manhattan_distance(galaxies_positions[i], galaxies_positions[j]) for i, j in pairs])
print(total)