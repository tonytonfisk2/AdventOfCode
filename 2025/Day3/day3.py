

with open('./data/day3.txt', 'r') as file:
    f = file.readlines()
    f = [x.replace("\n", "") for x in f]


def part1():
    ans = 0
    for line in f:
        d1 = 0
        d2 = 0
        for i in range(len(line)):
            d2 = max((d1 * 10) + int(line[i]), d2)
            if(int(line[i]) > d1):
                d1 = int(line[i])
                continue
        ans += d2
    return ans

print(part1())

def part2():
    total = 0

    for line in f:
        k = 12
        n = len(line) - k 
        stack = []

        for ch in line:
            while stack and n > 0 and stack[-1] < ch:
                stack.pop()
                n -= 1
            stack.append(ch)

        best = int(''.join(stack[:k]))
        total += best

    return total


print(part2())
  




                