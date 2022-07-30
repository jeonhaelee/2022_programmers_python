# 수식 최대화
# +, -, *

from itertools import permutations

def solution(expression):
    answer = 0
    numbers = []; cal = []
    num = ""
    for i in range(len(expression)):
        if expression[i].isdigit() :
            num += expression[i]
        else:
            cal.append(expression[i])
            numbers.append(int(num))
            num = ""
    
    cals = []
    cals.append(list(permutations(set(cal))))
    
    print(cals)
    
    # cals
    
    return answer

expression = "100-200*300-500+20"
print(solution(expression)) #60420