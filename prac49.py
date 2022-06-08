# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    zero = 0; same = 0
    for n in lottos:
        if n == 0:
            zero += 1
        elif n in win_nums:
            same += 1
    answer.append(same)
    answer.append(zero)
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums)) # [3, 5]