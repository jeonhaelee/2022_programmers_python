# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    
    zero = 0; same = 0
    for n in lottos:
        if n == 0:
            zero += 1
        elif n in win_nums:
            same += 1
            
    if same == 6:
        answer.append(1)
    elif same == 5:
        answer.append(2)
    elif same == 4:
        answer.append(3)
    elif same == 3:
        answer.append(4)
    elif same == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    same += zero
    if same == 6:
        answer.append(1)
    elif same == 5:
        answer.append(2)
    elif same == 4:
        answer.append(3)
    elif same == 3:
        answer.append(4)
    elif same == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums)) # [3, 5]