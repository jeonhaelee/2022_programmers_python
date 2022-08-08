# 점프와 순간이동
# 효율성 테스트 다시.

def solution(n):
    count = 0
    while n != 0 :
        n, m = n // 2, n % 2
        if m == 1 :
            count += 1
    return count

n = 5
print(solution(n)) # 2

n = 6
print(solution(n)) # 2