# 점프와 순간이동

def solution(n):
    ans = 0
    
    ans += 1
    place = 1
    
    state = True
    while state :
        result = place * 2
        if result > n:
            state = False
        else:
            place = result
    
    ans += n - place
    
    return ans

n = 5
print(solution(n)) # 2