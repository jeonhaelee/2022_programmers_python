# 문자열 압축


def make_short(s, n):
    result = ""
    
    target = s[0:n]
    target_count = 1
    
    for i in range(n, len(s), n):
        if s[i:i+n] == target:
            target_count += 1
        else:
            if target_count == 1:
                pass
            else:
                result += str(target_count)
            result += target
            target = s[i:i+n]
            target_count = 1
            
    if target_count == 1:
        pass
    else:
        result += str(target_count)
    result += target

    
    print(f'n : {n}, result : {result}')
    return result

def solution(s):
    answer = len(s)
    print(f'len(s) : {len(s)}')
    
    for n in range(1, len(s)):
        result = make_short(s, n)
        if len(result) < answer:
            answer = len(result)
        
    return answer

s = "aabbaccc"
print(solution(s)) # 7

s = "ababcdcdababcdcd"
print(solution(s)) # 9

s = "abcabcdede"
print(solution(s)) # 8

s = "abcabcabcabcdededededede"
print(solution(s)) # 14

s = "xababcdcdababcdcd"
print(solution(s)) # 17