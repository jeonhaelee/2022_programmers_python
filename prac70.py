# 점프와 순간이동

# 내 풀이
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

# 다른 사람 풀이 1
# -> 이진법을 이용한 풀이
def solution(n):
    return bin(n).count('1')

# 다른 사람 풀이 2
def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2
    return answer