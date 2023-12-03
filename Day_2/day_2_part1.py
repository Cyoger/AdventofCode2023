def calculate_sum_ids(game_info, red_cubes, green_cubes, blue_cubes):
    rounds = game_info.split("; ")
    for round_info in rounds:

        red_count, green_count, blue_count = 0, 0, 0

        cube_counts = round_info.split(", ")
        for cube in cube_counts:
            count, color = cube.strip().split(" ")
            count = int(count)
            if color == 'red':
                red_count += count
            elif color == 'green':
                green_count += count
            elif color == 'blue':
                blue_count += count

        if red_count > red_cubes or green_count > green_cubes or blue_count > blue_cubes:
            return False

    return True

        

total_corrected = 0
with open("input.txt", 'r') as r:
    for line in r:
        game_id, game_info = line.split(": ")
        game_id = int(game_id.split()[1])
        if calculate_sum_ids(game_info, 12, 13, 14):
            total_corrected += game_id

print(total_corrected)