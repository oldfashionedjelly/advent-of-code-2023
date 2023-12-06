cubes_per_color = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

end_chars = {":", ";", ",", "\n"}

def get_game_ids_sum(lines: list[str]) -> int:
    game_ids_sum = 0

    for line in lines:
        line = line.lower()
        game_id = 0
        word_chunk = ""
        number_chunk = ""

        for char in line:
            if char in end_chars:
                if word_chunk == "game":
                    game_id = int(number_chunk)
                elif word_chunk in cubes_per_color and int(number_chunk) > cubes_per_color[word_chunk]:
                    game_id = 0

                word_chunk = ""
                number_chunk = ""
            elif char.isalpha():
                word_chunk += char
            elif char.isdigit():
                number_chunk += char

        game_ids_sum += game_id
    return game_ids_sum


with open("results.txt", "r", encoding="utf-8") as f:
    print(get_game_ids_sum(f.readlines()))
