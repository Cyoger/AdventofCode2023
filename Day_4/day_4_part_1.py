def calculate_total(points):
    if points == 0:
        return 0
    return 2 ** (points - 1)
    
def get_card_sum(win_nums, card_nums):
    numbers1 = [int(num) for num in win_nums.split()]
    numbers2 = [int(num) for num in card_nums.split()]

    common_numbers = [num for num in numbers1 if num in numbers2]
    total_points = 0
    points = len(common_numbers)
    total_points += calculate_total(points)
    
    return total_points 
     
        

total_sum = 0

with open("input.txt") as r:
    
    for line in r:
        winning_nums, nums_in_card = line.split("|")
        game_name, winning_nums = winning_nums.split(": ")

        points = get_card_sum(winning_nums, nums_in_card)
        total_sum += points 
        
print(total_sum)
