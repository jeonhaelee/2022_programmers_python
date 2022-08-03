# 타겟넘버
# 다시
# target으로 만들 수 있는 +, - 조합 찾은 후
# 같은 숫자끼리 +, - 순서 바꿔서??

import math

def solution(numbers, target):
    answer = 0

    cal = []
    idx = 0
    result = 0
    while idx < len(numbers):
        if result < target:
            result += numbers[idx]
            cal.append('+')
            idx += 1
        else:
            result -= numbers[idx]
            cal.append('-')
            idx += 1

    print(cal)
    print(result)
    
    
    
    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5