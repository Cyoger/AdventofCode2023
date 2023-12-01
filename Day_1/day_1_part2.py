def find_digits_in_string(s):
    digit_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    digits = []

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if substring.isdigit():
                digits.append(int(substring))
            elif substring in digit_words:
                digits.append(digit_words[substring])

    return digits

def first_and_last(s):
    digits = find_digits_in_string(s)
    if not digits:
        return None, None
    return digits[0], digits[-1]


with open('/home/AdventofCode2023/Day_1/input.txt') as r:
    list = r.readlines()
    
num = 0  
total_sum = 0 
for i,x in enumerate(list):
    f, l = first_and_last(list[i])

    print(f,l)
    num = str(f) + str(l)

    
    total_sum += int(num)

print(total_sum)