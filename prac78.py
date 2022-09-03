# 타겟 넘버


# 내 풀이
from itertools import product

def get_cal(numbers, cal, target):
    
    result = 0
    
    for i in range(len(numbers)):
        if cal[i] == "+":
            result += numbers[i]
        else:
            result -= numbers[i]                
    
    return result
    
    
    
def solution(numbers, target):
    answer = 0
    li = ["+", "-"]
    cal_li = list(set(product(li, repeat = len(numbers))))
    print(cal_li)
        
    for cal in cal_li:
        result = get_cal(numbers, cal, target)
        if result == target:
            print(f'cal : {cal}')
            print(f'result : {result}')
            answer += 1
            
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target)) # 2


# 다른 사람 풀이1
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
    
# 다른 사람 풀이2
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)