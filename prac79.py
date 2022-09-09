# 이진 변환 반복하기


# 내 풀이
import sys
sys.setrecursionlimit(10**7)

def get_s(s, answer):
    
    after_s = s.replace("0", "")
    answer[0] += 1
    answer[1] += len(s) - len(after_s)

    s = bin(int(len(after_s)))
    s = s[2:]
    
    return s

    
def solution(s):

    answer = [0, 0]
    
    while s != "1":
        s = get_s(s, answer)

    return answer

s = "110010101001"
print(solution(s)) # [3,8]


# 다른 사람 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]