# 타겟 넘버

from itertools import permutations

def get_result(numbers, cal, target):
    
    result = numbers[0]
    for c in cal:
        if c == 0:
            continue
        if result >= target:
            result -= numbers[c]
        else:
            result += numbers[c]
    
    return result
    
    
    
def solution(numbers, target):
    answer = 0
    l = [i for i in range(0, len(numbers))]
    cal_li = list(set(permutations(l)))
    print(cal_li)
        
    for cal in cal_li:
        result = get_result(numbers, cal, target)
        if result == target:
            answer += 1
            
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5

