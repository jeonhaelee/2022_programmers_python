import sys
sys.setrecursionlimit(10000)

def pivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    answer = pivo(n-2) + pivo(n-1)
    return answer

def solution(n):
    answer = pivo(n)
    return int(answer/1234567)

n = 3
print(solution(n))