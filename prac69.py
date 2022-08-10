# 예상 대진표

def solution(n,a,b):
    answer = 0
    
    if a > b:
        a, b = b, a
    
    while n != 1:
        standard = n//2
        if a < standard and b > standard:
            answer += 1
    
    return answer

n = 8
a = 4
b = 7
print(solution(n,a,b)) # 3