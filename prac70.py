# 점프와 순간이동

def go_2multi(now, n):
    counts = []
    while True:
        get = now * 2
        if get > n:
            count += (n-now)
            counts.append(count)
            break
        elif get == n:
            counts.append(count)
            break
        else: now = get
    
    return counts


def solution(n):
    ans = 0
    now = 0; count = 0
    
    counts = []
    for i in range(n):
        now = i
        
        if now == 0:
            count += 1
            continue
        
        counts.extend(go_2multi(now, n))
    
    print(counts)

    return ans

n = 5
print(solution(n)) # 2

n = 6
print(solution(n)) # 2