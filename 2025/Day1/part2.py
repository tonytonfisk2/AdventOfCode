password = 50
count = 0
passed = 0

file_path = '../data/day1.txt'

with open(file_path, 'r') as f:
    data = f.read().splitlines() 


for d in data:
    rotation = d[:1]
    value = int(d[1:])

    if(rotation == 'R'):
        for i in range(value):
            password += 1
            if(password % 100 == 0):
                passed += 1 
    else:
        for i in range(value):
            password -= 1
            if(abs(password) % 100 == 0):
                passed += 1

    password % 100

"""
Boundary Check
for d in data:
    rotation = d[:1]
    value = int(d[1:])
    old_password = password 

    if(rotation == 'R'):
        password += value
        passed += password // 100 

    else:
        password -= value
        passed += (old_password - 1) // 100 - (password - 1) // 100
    
    password = password % 100
"""

print(passed)
                             