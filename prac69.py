# 예상 대진표

import math

def get_2(n):
    count = 0
    while n != 1:
        count += 1
        n = n//2
    return count


def solution(n,a,b):
    answer = 0
    
    if a > b:
        a, b = b, a
    
    standard = n//2
    if a <= standard and b > standard:
        answer += get_2(n)
    
    return answer

n = 8
a = 4
b = 7
print(solution(n,a,b)) # 3