# 이진 변환 반복하기
# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return


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