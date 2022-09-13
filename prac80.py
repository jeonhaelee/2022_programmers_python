# 괄호 회전하기


def before_check(s):
    word_li = [[0, 0], [0, 0], [0, 0]]
    
    for w in s:
        if w == "[":
            word_li[0][0] += 1
        elif w == "]":
            word_li[0][1] += 1
        elif w == "(":
            word_li[1][0] += 1
        elif w == ")":
            word_li[1][1] += 1
        elif w == "{":
            word_li[2][0] += 1
        elif w == "}":
            word_li[2][1] += 1
        
    for word in word_li:
        if word[0] != word[1]:
            return False

    return True

        
def check_true(s):
    result = 0
    
    return result
    
    
def solution(s):
    answer = 0
    
    if len(s) % 2 != 0:
        return 0
    
    if not before_check(s):
        return 0
    
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