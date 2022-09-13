# 괄호 회전하기

def check_true(s):
    result = 0
    
    return result
    
def solution(s):
    answer = 0
    count = 0
    while count < len(s):
        s = s[1:] + s[0]
        result = check_true(s)
        if result:
            return result
        else:
            count += 1
        
    return answer

s = "[](){}"
print(solution(s)) # 3

s = "}]()[{"
print(solution(s)) # 2

s = "[)(]"
print(solution(s)) # 0