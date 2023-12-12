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


def get_empty_rows(galaxy: list[list[str]]) -> list[int]:
    empty_rows = []
    for idx, row in enumerate(galaxy):
        if all([char == "." for char in row]):
            empty_rows.append(idx)
    return empty_rows
    

def get_empty_cols(galaxy: list[list[str]]) -> list[int]:
    empty_cols = []
    for idy in range(len(galaxy[0])):
        if all([galaxy[idx][idy] == "." for idx in range(len(galaxy))]):
            empty_cols.append(idy)
    return empty_cols


def get_galaxies_positions(galaxy: list[list[str]]) -> dict[int, tuple[int, int]]:
    return {
        galaxy[idx][idy]: (idx, idy)
        for idx in range(len(galaxy))
        for idy in range(len(galaxy[0]))
        if galaxy[idx][idy] != "."
    }


def manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return sum([abs(point1[0] - point2[0]), abs(point1[1] - point2[1])])


def get_extra_for_crossing_empties(
    point1: tuple[int, int], 
    point2: tuple[int, int],
    empty_rows: list[int], 
    empty_cols: list[int],
) -> int:
    extra = 0
    min_x, max_x = (point1[0], point2[0]) if point1[0] < point2[0] else (point2[0], point1[0])
    for row in empty_rows:
        if min_x < row < max_x:
            extra += 1_000_000 - 1
            
    min_y, max_y = (point1[1], point2[1]) if point1[1] < point2[1] else (point2[1], point1[1])
    for col in empty_cols:
        if min_y < col < max_y:
            extra += 1_000_000 - 1
    
    return extra
    

galaxy, num_galaxies = read_galaxy()
galaxies_positions = {
    galaxy[idx][idy]: (idx, idy)
    for idx in range(len(galaxy))
    for idy in range(len(galaxy[0]))
    if galaxy[idx][idy] != "."
}
pairs = [(i, j) for i in range(num_galaxies) for j in range(i, num_galaxies) if i < j]
empty_rows = get_empty_rows(galaxy)
empty_cols = get_empty_cols(galaxy)
total = sum([
    (
        manhattan_distance(galaxies_positions[i], galaxies_positions[j]) 
        + get_extra_for_crossing_empties(galaxies_positions[i], galaxies_positions[j], empty_rows, empty_cols)
    )
    for i, j in pairs
])
print(total)