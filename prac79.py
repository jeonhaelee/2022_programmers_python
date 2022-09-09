# 이진 변환 반복하기
# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return


import sys
sys.setrecursionlimit(10**7)

answer = [0, 0]

def solution(s):
    global answer
    
    after_s = s.replace("0", "")
    answer[1] += len(s) - len(after_s)
    answer[0] += 1

    s = bin(int(len(after_s)))
    
    if s == 1:
        return answer
    else:
        solution(s)

s = "110010101001"
print(solution(s)) # [3,8]