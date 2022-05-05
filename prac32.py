def pivo(n):
    answer = pivo(n-2) + pivo(n-1)
    return answer

def solution(n):
    answer = pivo(n)
    return int(answer/1234567)

n = 3
print(solution(n))