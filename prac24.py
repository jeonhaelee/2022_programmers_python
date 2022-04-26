
# 스택 이용
def solution(s):
    answer = 0
    
    result = []
    result.append(s[0])
    
    for i in range(1, len(s)):
        if len(result) == 0:
            result.append(s[i])
            continue
        if result[-1] == s[i]:
            result.pop()
        else: result.append(s[i])
        
    if len(result) == 0:
        answer = 1
        return answer
    else:
        return answer
