

with open('../data/day2.txt', 'r', encoding='UTF-8') as file:
        data = file.read().replace('\n', '')
        ranges = data.split(',')

def check_sequence(num):
    num = str(num)
    return True if num[:len(num)//2] == num[len(num)//2:] else False 

def part1():
    r_tuple = [tuple(map(int,r.split("-"))) for r in ranges]
    ans = 0
    for limits in r_tuple:
        lower, upper = limits
        diff = upper - lower
        curr = lower
        for _ in range(diff + 1):
            if(check_sequence(curr)):
                ans += curr
            curr += 1
    return ans

def check_sequence2(num):
    #Check potential sequences. #Potential Sequences = len(num) % #Ps == 0

    num = str(num)
    
    for i in range(1, len(num)//2):
        pattern = ""
        if(len(num) % (i + 1) == 0):
            pattern = num[:i + 1]
            ans = pattern * (len(num) // len(pattern))
            if(ans == num):
                return True
    return False

        

def part2():
    r_tuple = [tuple(map(int,r.split("-"))) for r in ranges]
    ans = 0
    for limits in r_tuple:
        lower, upper = limits
        diff = upper - lower
        curr = lower
        for _ in range(diff + 1):
            if(check_sequence2(curr)):
                ans += curr
            curr += 1
    return ans

#print(check_sequence2(1188511885))
print(part2())


