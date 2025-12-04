with open('./data/day4.txt', 'r', encoding='utf-8') as file:
    f = file.readlines()
    f = [x.strip() for x in f]


padded = [[0] *  (len(f[0]) + 2)]

for row in f:
    padded.append([0] + list(row) + [0])

padded.append([0] * (len(f[0]) + 2))


dirs = [(0,-1), (-1,0), (0,1), (1,0),
        (-1,-1), (1,-1), (-1,1), (1,1)] 

def part1():
    total = 0
    for y, row in enumerate(padded[1:-1], start = 1):
        for x, col in enumerate(row[1:-1], start = 1):
            count = 0
            if(padded[y][x] == '@'):
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    neighbor = padded[ny][nx]
                    if(neighbor == '@'):
                        count += 1
                if(count < 4):
                    total += 1
    return total 



def part2():
    total = 0

    while True:
        remove = []
        for y, row in enumerate(padded[1:-1], start = 1):
            for x, col in enumerate(row[1:-1], start = 1):
                count = 0
                if(padded[y][x] == '@'):
                    for dx, dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        neighbor = padded[ny][nx]
                        if(neighbor == '@'):
                            count += 1
                    if(count < 4):
                        total += 1
                        remove.append((x,y))

        for rx, ry in remove:
            padded[ry][rx] = '.'
        
        if(len(remove) == 0):
            break

    return total

    
print(part1())
print(part2())
