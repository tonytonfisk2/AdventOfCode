password = 50
count = 0

file_path = '../data/day1.txt'

with open(file_path, 'r') as f:
    data = f.read().splitlines() 

for d in data:
    rotation = d[:1]
    value = int(d[1:])
    if(rotation == 'R'):
        password += value
    else:
        password -= value
    
    password = password % 100
    if(password == 0):
        count += 1
        print(password)

print(count)
