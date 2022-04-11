

def solution(num):
    answer = ''
    sub_answer = ''
    
    num, rest = divmod(num, 3)
    if rest == 1:
        sub_answer += '1'
    elif rest == 2:
        sub_answer += '2'
    else: sub_answer += '4'
    
    while num > 0:
        num, rest = divmod(num, 3)
        if rest == 1:
            sub_answer += '1'
        elif rest == 2:
            sub_answer += '2'
        else: sub_answer += '4'
    
    for i in range(len(sub_answer)-1,-1,-1):
        answer += sub_answer[i]
        
    return int(answer)


n = 3
print(solution(n))