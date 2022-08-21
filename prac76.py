# 멀리 뛰기 - 1칸 또는 2칸씩

from itertools import permutations

def solution(n):
    answer = 0
    
    if n % 2 == 0:
        two_num = n // 2
        for two_count in range(two_num):
            num_li = [1] * (n - two_count)
            two_li = [2] * two_count
            num_li.extend(two_li)
            result = list(permutations(num_li))
            answer += len(result)
            
    else:
        two_num = n // 2
        num_li = [1] * (n - two_count + 1)
        two_li = [2] * two_count
        num_li.extend(two_li)
        result = list(permutations(num_li))
        answer += len(result)
        
    return answer % 1234567

n = 4
print(solution(n)) # 5