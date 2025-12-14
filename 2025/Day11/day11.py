from collections import deque

dset = {}

with open('../data/day11.txt', 'r') as file:
    lines = [line.replace(':', '').strip().split(' ') for line in file]
    dset = {k[0]: k[1:] for k in lines}

start = 'you'


def part1(graph, start):
    paths = 0
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if(n == 'out'):
                paths += 1
            elif(n == start):
                continue
            else:
                queue.append(n)

    return paths

start2 = 'svr'

memo = {} #DP (node, path, seen)

def part2_memo(graph, node,fft,dac):
    if node == 'out':
        return 1 if fft and dac else 0
    key = (node, fft, dac)

    if key in memo:
        return memo[key]
    
    fft = fft or (node == 'fft')
    dac = dac or (node == 'dac')

    total = 0
    
    for nxt in graph[node]:
        total += part2_memo(graph, nxt, fft, dac)

    memo[key] = total

    return total 

def part2(graph, start):
    
    paths = 0 
    stack = []
    stack = [(start, {start}, False, False)]
    
    while stack: 
        
        node, seen, fft, dac = stack.pop()
        if(node == 'fft'):
            fft = True
        elif(node == 'dac'):
            dac = True
        elif(node == 'out'):
            if(dac and fft):
                paths += 1
            continue
        
        if node in graph:
            for n in (graph[node]):
                if n not in seen:
                    stack.append((n, seen | {n}, fft, dac))

    return paths

#print(part1(dset, start))
print(part2_memo(dset, 'svr', False, False))
