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
    sub_list = []
    
    li = list(dartResult)
    
    number = ""
    for i in range(len(li)):
        if li[i].isdigit():
            number += li[i]
        elif li[i] in ("S","D","T"):
            done_num = int(number)
            number = ""
            
            get_num = get_number(li[i])
            
            sub = math.pow(done_num, get_num)
            sub_list.append(sub)
 
        elif li[i] == "#":
            sub_list[-1] = -sub_list[-1]       
        
        elif li[i] == "*":
            if len(sub_list) == 1:
                sub_list[-1] = sub_list[-1] * 2
            else:
                sub_list[-2] = sub_list[-2] * 2
                sub_list[-1] = sub_list[-1] * 2
                
    for sub in sub_list:
        answer += sub
        
    return int(answer)


dartResult = "1T2D3D#"
print(solution(dartResult)) 
