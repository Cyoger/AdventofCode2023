def get_cards(win_nums, card_nums):
    numbers1 = [int(num) for num in win_nums.split()]
    numbers2 = [int(num) for num in card_nums.split()]

    common_numbers = [num for num in numbers1 if num in numbers2]
    total_points = 0
    points = len(common_numbers)
    return points
    

cards = []
with open("input.txt") as r:
    
    for line in r:
        winning_nums, nums_in_card = line.split("|")
        game_name, winning_nums = winning_nums.split(": ")
        cards.append(get_cards(winning_nums, nums_in_card))
        
instances = [1] * len(cards)

for i,x in enumerate(cards):
    for j in range(i+1, i+1+x):
        instances[j] += instances[i]
        
print(sum(instances))