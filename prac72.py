# 조이스틱

def solution(name):
    answer = 0
    
    for n in name:
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n))
    print(ord(name[0]))
    return answer

name = "JEROEN"
print(solution(name))