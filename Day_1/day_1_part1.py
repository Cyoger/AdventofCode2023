def first_and_last(s):
    f = None
    l = None
    
    for char in s:
        if char.isdigit():
            f = char
            break
    for char in reversed(s):
        if char.isdigit():
            l = char
            break

    return f, l

with open('../input.txt') as r:
    list = r.readlines()
num = 0  
total_sum = 0 
for i,x in enumerate(list):
    f, l = first_and_last(list[i])

    num = f + l
    
    total_sum += int(num)
 
    
print(total_sum)