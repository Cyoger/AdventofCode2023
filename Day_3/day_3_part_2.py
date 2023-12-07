import re
from collections import defaultdict
from math import prod

def part_sum_gears(lines):


    symbols = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c not in "1234567890.":
                symbols[(x, y)] = c

    gears = defaultdict(list)
    part_numbers_sum = 0
    for y, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            for (s_x, s_y), c in symbols.items():
                if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                    num = int(match.group())
                    part_numbers_sum += num
                    if c == "*":
                        gears[(s_x, s_y)].append(num)
                    break
                
    return sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2)


with open("input.txt") as r:
    lines = r.read().split("\n")

part_sum = part_sum_gears(lines)
print(part_sum)