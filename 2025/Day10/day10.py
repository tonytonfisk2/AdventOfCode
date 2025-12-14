#Nestled for loop.
#Save state for each element/combination
#While looping check in the saved state dict if ans exist thumbsup

from collections import defaultdict
from z3 import *

with open('../data/day10.txt', 'r') as file:
    lines = [line.strip().split(' ') for line in file]



def parse_data(lines):
    a = []
    b = [row[1:-1] for row in lines]
    c = [row[-1] for row in lines]

    for row in lines:
        d = [0] * len(row)
        for idx, item in enumerate(row[0][1:-1]):
            if(item == '.'):
                continue
            else:
                d[idx] = 1
        a.append(d)

    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = b[i][j].replace('(', '').replace(')', '').split(',')

    for i in range(len(c)):
        c[i] = c[i].replace('{', '').replace('}', '').split(',')

    return a, b , list(zip(b,c))

def find_combinations(a):
    if len(a) == 0:
        return [[]]
    
    first_item = a[0]
    r_combos = find_combinations(a[1:])

    result = []
    for combo in r_combos:
        result.append(combo)
        result.append([first_item] + combo)

    return result

def part1(a, b):
    combs = []
    total = 0
    for idx, row in enumerate(b):
        min_val = 1000
        target = a[idx]
        combs = sorted(find_combinations(row), key=len)
        for items in combs:
            state = [0] * len(target)
            for item in items:
                for n in item:
                    state[int(n)] = abs(state[int(n)] - 1)

            if(state == target):
                min_val = min(len(items), min_val)
        total += min_val

    return total

def solve_eq(c):
    #init z3 variables
    buttons, joltage = c[0], c[1]
    b_len = len(buttons)
    j_len = len(joltage)
    counters = [[] for _ in range(j_len)]

    for b, button in enumerate(buttons):
        for c in button:
            counters[int(c)].append(b) 

    btn = IntVector('btn', b_len)
    presses = Int('presses')

    

    s = Optimize()

    for b in range(b_len):
        s.add(btn[b] >= 0)

    for c in range(len(counters)):
        s.add(sum(btn[b] for b in counters[c]) == joltage[c])

    s.add(sum(btn) == presses)
    s.minimize(presses)

    s.check()

    m = s.model()

    presses = m.eval(presses).as_long()
        
    return presses

def part2(c):
    total = 0

    for m in c:
        presses = solve_eq(m)
        total += presses

    return total

a, b, c = parse_data(lines)


print(part1(a, b))
print(part2(c))