import numpy as np

with open('../data/day8.txt', 'r') as file:
    lines = [[float(x) for x in line.strip().split(',')] for line in file]

#Distance Formula = sqrt((p1 - q1)^2 + (p2 - q2)^2 + (p3 - q3)^2)
#Kruskals algorithm 

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

def part1():
    edges = []
    circuits = [set() for _ in range(len(lines))]
    for idx, p1 in enumerate(lines):
        for p2 in lines[idx + 1:]:
            edges.append([dist(p1, p2), (p1,p2)])

    #print(sorted(edges)[0:10])

    for idx, itm in enumerate(sorted(edges)):
        if idx >= 1000:
            break
  
        p1 = itm[1][0]
        p2 = itm[1][1]
        for j in range(len(circuits)):
            if((p1[0], p1[1], p1[2]) in circuits[j] or (p2[0], p2[1], p2[2]) in circuits[j]):
                circuits[j].add((p1[0], p1[1], p1[2]))
                circuits[j].add((p2[0], p2[1], p2[2]))
            elif(len(circuits[j]) == 0):
                circuits[j].add((p1[0], p1[1], p1[2]))
                circuits[j].add((p2[0], p2[1], p2[2]))
                break

    changed = True
    while changed:
        changed = False
        for idx, item in enumerate(circuits):
            for jdx, jtem in enumerate(circuits[idx + 1:], start = idx + 1):
                if(len(circuits[idx]) == 0):
                    continue
                if(circuits[idx].intersection(circuits[jdx])):
                    circuits[idx] = circuits[idx].union(circuits[jdx])
                    circuits[jdx] = set()   
                    changed = True
          
    circuits = [c for c in circuits if c]
    sizes = sorted([len(c) for c in circuits], reverse= True)
    return sizes[0] * sizes[1] * sizes[2]

def part2():
    edges = []
    circuits = [set() for _ in range(len(lines))]
    all_points = set()
    for idx, p1 in enumerate(lines):
        all_points.add((p1[0], p1[1], p1[2]))
        for p2 in lines[idx + 1:]:
            edges.append([dist(p1, p2), (p1,p2)])

    last_p1, last_p2 = None, None
    print(sorted(edges,reverse=True)[0])
    for idx, itm in enumerate(sorted(edges)):
        if len(all_points) == 0:
            break

        p1 = itm[1][0]
        p2 = itm[1][1]
        p1_tuple = (p1[0], p1[1], p1[2])
        p2_tuple = (p2[0], p2[1], p2[2])
        for j in range(len(circuits)):
            if(p1_tuple in circuits[j] or p2_tuple in circuits[j]):
                circuits[j].add(p1_tuple)
                circuits[j].add(p2_tuple)
                all_points.discard(p1_tuple)
                all_points.discard(p2_tuple)
                last_p1, last_p2 = p1, p2
                break
            elif(len(circuits[j]) == 0):
                circuits[j].add(p1_tuple)
                circuits[j].add(p2_tuple)
                all_points.discard(p1_tuple)
                all_points.discard(p2_tuple)
                last_p1, last_p2 = p1, p2
                break

    return int(last_p1[0] * last_p2[0])

print(part1())
print(part2())