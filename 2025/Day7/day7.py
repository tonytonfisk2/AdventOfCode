with open('../data/day7.txt', 'r') as file:
    lines = [line.strip() for line in file]

ans = set()
src = None
def part1():
    total = 0
    for row, line in enumerate(lines):
        for col, item in enumerate(line):
            if(item == 'S'):
                src = (row + 1, col)
                ans.add((row + 1,col))
            elif(item == '^'):
                ans.add((row,col + 1))
                ans.add((row,col - 1))
                if((row - 1, col) in ans):
                    total += 1
            elif((row - 1, col) in ans): 
                ans.add((row, col))
    return total, src

def part2():
    total = [0] * len(lines[0])
    print(total)
    for row, line in enumerate(lines):
        for col, item in enumerate(line):
            if(item == 'S'):
                total[col] += 1
            elif(item == '^'):
                total[col + 1] += total[col]
                total[col - 1] += total[col]
                total[col] = 0
    print(total)
    return sum(total)



print(part1())
print(part2())
