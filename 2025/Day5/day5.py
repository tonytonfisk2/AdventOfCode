interval = []
fresh_ingredients = []

with open('../data/day5.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if '-' in line:
            interval.append(tuple(map(int,line.strip().split('-'))))
        else:
            if(line == '\n'):
                continue
            fresh_ingredients.append(int(line.strip()))

def part1():

    total = 0

    for fi in fresh_ingredients:
        for l, r in interval:
            if int(fi) in range(l, r):
                total += 1
                break

    return total


# 3-5
# 10-14
# 16-20
# 12-18

#(3,5) (10, 14), (16,20), (12,18) 
# add to arr 
# check and merge
def part2():
    ranges = []
    r = sorted(interval)

    for l,r in r:
        ranges.append((l,r))
        n = len(ranges) - 2
        tl, tr = l, r
        while n >= 0 and ranges:
            l2, r2 = ranges[n] 
            if(tl and tr in range(l2 - 1,r2 + 1)):
                # pop l and r dont need it
                ranges.pop(n + 1)
                tl, tr = l2, r2
            elif(tl < l2 and tr > r2):
                # pop l2 and r2
                ranges.pop(n)
            elif(l in range(l2 - 1,r2 + 1) and tr > r2):
                # merge (l2, r)
                ranges.pop(n)
                ranges[n] = (l2, tr)
                tl, tr = l2, tr
            elif(tl < l2 and tr in range(l2 - 1,r2 + 1)):
                ranges.pop(n)
                ranges[n] = (tl, r2)
                tl, tr = tl, r2
                # merge (l, r2)

            n -= 1
    return sum([(r - l) + 1 for l, r in ranges])





print(part1())
print(part2())