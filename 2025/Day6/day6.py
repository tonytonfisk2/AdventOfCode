
from math import prod
nums = []
symbols = []
p2 = []
with open('../data/day6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split()
        for x in line:
            if(x == ''):
                continue
            if(x.isdigit()):
                nums.append(int(x))
            else:
                symbols.append(x)
    
with open('../data/day6.txt', 'r', encoding='utf-8') as file:
    p2 = [line for line in file]

print(2%len(symbols))

def part1():
    ans = nums[:len(symbols)]
    for idx , n in enumerate(nums[len(symbols):]):
        ans_idx = idx % len(symbols)
        if(symbols[ans_idx] == '+'):
            ans[ans_idx] += n
        else:
            ans[ans_idx] *= n
    return sum(ans)

def part2():
    total = 0
    ans = []
    operator = None
    for col in range(len(p2[0])):
        num = ''
        for row in p2:
            if(col >= len(row)):
                break
            if(row[col] not in ['', ' ', '\n', '*', '+']):
                num += row[col]
            elif(row[col] == '*'):
                operator = '*'

            elif(row[col] == '+'):
                operator = '+'

        if(num.isnumeric()):
            ans.append(int(num))
        else:
            if(operator == '+'):
                total += sum(ans)
            else:
                total += prod(ans)
            ans = []

    return total

print(part1())
print(part2())