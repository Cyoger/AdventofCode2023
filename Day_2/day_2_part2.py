def calculate_power(game_info):
    max_red, max_green, max_blue = 0, 0, 0
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
                
        max_red = max(max_red, red_count)
        max_green = max(max_green, green_count)
        max_blue = max(max_blue, blue_count)

    return max_red * max_green * max_blue

total_power = 0
with open("input.txt", 'r') as r:
    for line in r:
        game_id, game_info = line.split(": ")
        total_power += calculate_power(game_info)

print(total_power)
