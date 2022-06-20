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
    print(li)
    
    number = ""
    while len(li) > 0:
        
        if li[0].isdigit():
            number += li[0]
            del li[0]
            print(li)
            
        else:
            done_num = int(number)
            number = ""
            
            get_num = get_number(li[0])
            del li[0]
            print(li)
            
            sub = math.pow(done_num, get_num)
            sub_list.append(sub)
            
            if len(li) == 0:
                answer += sub_list[0]
                break
                
            if li[0] == "*":
                answer += sub_list[0] * 2
                answer += sub_list[1] * 2
                sub_list = []
                del li[0]
                print(li)

            elif li[0] == "#":
                answer += sub_list[0]
                answer -= sub_list[1]
                sub_list = []
                del li[0]
                print(li)

            else:
                for sub in sub_list:
                    answer += sub
            
    return int(answer)

# def solution(dartResult):
#     answer = 0
    
#     li = list(dartResult)
#     print(li)
    
#     number = ""
#     while len(li) > 0:
        
#         if li[0].isdigit():
#             number += li[0]
#             del li[0]
#             print(li)
            
#         else:
#             done_num = int(number)
#             number = ""
            
#             get_num = get_number(li[0])
#             del li[0]
#             print(li)
            
#             sub = math.pow(done_num, get_num)
            
#             if len(li) == 0:
#                 answer += sub
#                 break
                
#             if li[0] == "*":
#                 answer = answer * 2
#                 answer += sub * 2
#                 del li[0]
#                 print(li)

#             elif li[0] == "#":
#                 answer -= sub
#                 del li[0]
#                 print(li)

#             else:
#                 answer += sub
            
#     return int(answer)

dartResult = "1S2D*3T" # 37
print(solution(dartResult)) 

dartResult = "1D2S3T*"
print(solution(dartResult)) # 59