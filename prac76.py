# 멀리 뛰기 - 1칸 또는 2칸씩

from itertools import permutations

def solution(n):
    answer = 0
    
    if n % 2 == 0:
        two_num = n // 2
        for i in range(two_num + 1):
            num_li = [1] * (n - i * 2)
            print(f'num_li : {num_li}')
            two_li = [2] * i
            print(f'two_li : {two_li}')
            num_li.extend(two_li)
            print(f'num_li : {num_li}')
            result = list(set(permutations(num_li)))
            print(f'result : {result}')
            
            answer += len(result)
            
    else:
        two_num = n // 2
        num_li = [1] * (n - i * 2 + 1)
        two_li = [2] * i
        num_li.extend(two_li)
        result = list(permutations(num_li))
        answer += len(result)
        
    return answer % 1234567

n = 4
print(solution(n)) # 5