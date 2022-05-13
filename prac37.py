import sys
sys.setrecursionlimit(10**7)

def solution(n):
    if n == 0: return 0
    if n == 1: return 1
    answer = solution(n-1) + solution(n-2)
    return answer % 1234567

n = 5
print(solution(n))