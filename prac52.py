# [1차] 다트 게임
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 
# 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산.

import math

def get_number(s):
    if s == "S":
        return 1
    elif s == "D":
        return 2
    elif s == "T":
        return 3
    
def solution(dartResult):
    answer = 0
    
    li = list(dartResult)
    print(li)
    
    number = ""; sub = 0
    
    i = 0
    while i < len(li):
        
        if li[i].isdigit():
            number += li[i] 
            i += 1
            continue
        
        sub = math.pow(int(number),get_number(li[i]))

        if i != len(li) - 1:
            
            if li[i+1] == "*":
                answer = answer * 2
                answer += sub * 2
                number = ""
                sub = 0
                i += 2
            elif li[i+1] == "#":
                answer -= sub
                number = ""
                sub = 0
                i += 2
            else:
                answer += sub
                number = ""
                sub = 0
                i += 1
            
    return answer

dartResult = "1S2D*3T"
answer = 37
print(solution(dartResult)) 

dartResult = "1D2S#10S"
answer = 9
print(solution(dartResult)) 