# 타겟 넘버

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

