# [1차] 다트 게임
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 
# 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산.

# 내 풀이

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


# 다른 사람 풀이 1

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 다른 사람 풀이 2

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)