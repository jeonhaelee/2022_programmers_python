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

def get_sub_sum(sub_list):
    ans = 0
    for sub in sub_list:
        ans += sub
    return ans
    
    
def solution(dartResult):
    answer = 0
    sub_list = []
    
    li = list(dartResult)
    print(li)
    
    number = ""
    while len(li) > 0:
        
        if li[0].isdigit():
            number += li[0]
            del li[0]
            
        else:
            done_num = int(number)
            number = ""
            
            get_num = get_number(li[0])
            del li[0]
            
            sub = math.pow(done_num, get_num)
            
            
            
            if li[0] == "#":
                sub_list.append(-sub)
                del li[0]
            else:
                sub_list.append(sub)
                
            print(f'sub : {sub}')
            print(f'sub_list : {sub_list}')
            
            if len(li) == 0:
                print(f'sub_list : {sub_list}')
                answer += get_sub_sum(sub_list)
                print(f'answer : {answer}')
                break
            
            if li[0] == "*":
                if len(sub_list) == 1:
                    answer += sub_list[-1] * 2
                    del sub_list[-1]
                    print(f'answer : {answer}')
    
                else:
                    answer += sub_list[-1] * 2
                    del sub_list[-1]
                    answer += sub_list[-1] * 2
                    del sub_list[-1]
                    print(f'answer : {answer}')
                    
                del li[0]
                answer += get_sub_sum(sub_list)
                print(f'answer : {answer}')
                sub_list = []
        
            
    return int(answer)


dartResult = "1T2D3D#"
print(solution(dartResult)) 
