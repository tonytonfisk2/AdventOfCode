
import matplotlib.pyplot as plt
import numpy as np


with open('../data/day9.txt', 'r') as file:
    lines = [tuple(map(int, line.strip().split(','))) for line in file]


def part1():
    a = [0 for _ in range(len(lines))]

    for idx, (w, h) in enumerate(lines):
        area = 0

        for w2, h2 in lines[idx + 1:]:
            area = (abs(w2 - w) + 1) * (abs(h2 - h) + 1)
            a[idx] = max(a[idx], area)
    
    return max(a)

def print_grid(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))
    print()  

def grid():

    unique_w = sorted(set(w for w, _ in lines))
    unique_h = sorted(set(h for _, h in lines))

    w_to_idx = {w:i for i, w in enumerate(unique_w)}
    h_to_idx = {h:i for i, h in enumerate(unique_h)}

    height = len(unique_h)
    width = len(unique_w)

    grid = [[0 for _ in range(width)] for _ in range(height)]
    for w, h in lines:
        grid[h_to_idx[h]][w_to_idx[w]] = 1

    countY = [0 for _ in range(width)]
    for i in range(len(grid)):
        count = 0 
        
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1 
                countY[j] += 1
            elif count % 2 != 0:
                grid[i][j] = 1
            elif countY[j] % 2 != 0:
                grid[i][j] = 1

    for i in range(len(grid)):
        first = -1
        last = -1
        for j in range(len(grid[0])):
            if(grid[i][j] == 1):
                if(first == -1):
                    first = j
                last = j
            
        if first != -1 and last != -1:
            for k in range(first, last + 1):
                grid[i][k] = 1

    arr = np.array(grid)
    plt.figure(figsize=(8, 8))
    plt.imshow(arr, cmap="gray_r")
    plt.show()

    return grid, h_to_idx, w_to_idx


def part2(grid, h_to_idx, w_to_idx):
    a = [0 for _ in range(len(lines))]

    for idx, (w, h) in enumerate(lines):
        area = 0
        for w2, h2 in lines[idx + 1:]:
            w_idx = w_to_idx[w]
            w2_idx = w_to_idx[w2]
            h_idx = h_to_idx[h]
            h2_idx = h_to_idx[h2]

            min_width = min(w_idx, w2_idx)
            max_width = max(w_idx, w2_idx)
            min_height = min(h_idx, h2_idx)
            max_height = max(h_idx, h2_idx)

            flag = True

            for i in range(min_width, max_width + 1):
                if(grid[min_height][i] != 1 or grid[max_height][i] != 1):
                    flag = False
                    break
            if flag:
                for i in range(min_height, max_height + 1):
                    if(grid[i][max_width] != 1 or grid[i][min_width] != 1):
                        flag = False
                        break
                    
            if flag:
                area = (abs(w2 - w) + 1) * (abs(h2 - h) + 1)
                a[idx] = max(a[idx], area)
    return max(a)
    

print(part1())

g, h_to_idx, w_to_idx = grid()

print(part2(g, h_to_idx, w_to_idx))

