# N개의 최소공배수

import math

def solution(arr):
    answer = 0
    max_num = max(arr)
    
    i = max_num
    while True:
        count = 0
        for n in arr:
            if i % n != 0:
                count += 1
        
        if count == 0:
            answer = i
            break
        else:
            i *= 2
            
    return answer

arr = [2,6,8,14]
print(solution(arr)) # 168