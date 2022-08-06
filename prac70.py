# 점프와 순간이동

counts = []

def go_2multi(now, n, count):
    global counts 
    
    while True:
        get = now * 2
        go_1(get, n, count)
        if get > n:
            sub_count = (n-now)
            counts.append(count + sub_count)
            break
        elif get == n:
            counts.append(count)
            break
        else: now = get
    

def go_1(get, n, count):
    go_2multi(get + 1, n, count + 1)
    

def solution(n):
    global counts
    
    ans = 0
    now = 0
    
    
    count = 0
    counts = []
    for i in range(n):
        now = i
        
        if now == 0:
            count += 1
            continue
        
        go_2multi(now, n, count)
        count += 1
    
    counts.append(count)
    
    print(counts)

    ans = min(counts)
    return ans

n = 5
print(solution(n)) # 2

n = 6
print(solution(n)) # 2