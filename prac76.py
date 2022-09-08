# 멀리 뛰기


from itertools import permutations

def solution(n):
    answer = 0
    
    two_num = n // 2
    if n % 2 == 0:
        for i in range(two_num + 1):
            num_li = [1] * (n - i * 2)
            two_li = [2] * i
            num_li.extend(two_li)
            result = list(set(permutations(num_li)))
            answer += len(result)
            
    else:
        for i in range(two_num + 1):
            num_li = [1] * (n - i * 2)
            two_li = [2] * i
            num_li.extend(two_li)
            result = list(set(permutations(num_li)))
            answer += len(result)
        
    return answer % 1234567

n = 4
print(solution(n)) # 5

n = 3
print(solution(n)) # 3