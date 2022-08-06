# 점프와 순간이동
# 효율성 테스트 다시.
# 도착지점에서 0으로 돌아오는 법으로 생각해보자...
# 홀수와 짝수랑 관계가 있나?

def get_twice(num, count, n, counts):
    
    while True:
        if num * 2 > n:
            counts.append(count + n - num)
            break
        elif num * 2 == n:
            counts.append(count)
            break
        else:
            num *= 2
            get_twice(num, count, n, counts)
            get_twice(num + 1, count + 1, n, counts)
    

def solution(n):
    counts = []
    
    num = 1; count = 1
    get_twice(num, count, n, counts)
    
    ans = min(counts)
    
    return ans

n = 5
print(solution(n)) # 2

n = 6
print(solution(n)) # 2