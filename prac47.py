# 2 x n 타일링
# 세로의 길이가 2, 가로의 길이가 n
import math

def solution(n):
    answer = 1
    
    i = 1
    while 2*i <= n:
        answer += math.factorial(n-i)/(math.factorial(i)*math.factorial(n-2*i))
        i += 1
        
        
    return int(answer)

n = 4
print(solution(n))