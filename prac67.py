# N개의 최소공배수

import math


def get_min(arr):
    i = 1
    for i in range(2, min(arr)+1):
        count = 0
        for n in arr:
            if n % i == 0:
                count += 1
        if count == len(arr):
            return i
    return i


def solution(arr):
    answer = 1
    min_num = min(arr)
    
    i = get_min(arr)

    for num in arr:
        answer *= int(num / i)
    
    return answer * i

arr = [2,6,8,14]
print(solution(arr)) # 168