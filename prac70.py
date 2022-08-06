# 점프와 순간이동

import sys
sys.setrecursionlimit(10**7)

counts = []
target = 0

def go_2multi(now, count):
    global counts 
    global tarket
    
    while True:
        get = now * 2
        go_2multi(get + 1, count + 1)
        if get > target:
            sub_count = (n-now)
            counts.append(count + sub_count)
            break
        elif get == target:
            counts.append(count)
            break
        else: now = get
    

def solution(n):
    global counts
    global target
    target = n
    
    ans = 0
    now = 0
    count = 0
    for i in range(target):
        now = i
        
        if now == 0:
            count += 1
            continue
        
        go_2multi(now, count)
        count += 1
    
    counts.append(count)
    
    print(counts)

    ans = min(counts)
    return ans

# n = 5
# print(solution(n)) # 2

n = 6
print(solution(n)) # 2