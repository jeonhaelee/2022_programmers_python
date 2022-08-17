# 올바른 괄호

def solution(s):
    answer = True

    head = 0; tail = 0
    for w in s:
        if w == "(":
            head += 1
        elif w == ")":
            tail += 1
        
        if head < tail:
            return False
        
    if head != tail:
        return False
    else:
        return True

s = "()()"
print(solution(s)) # True

s = "(())()"
print(solution(s)) # True

s = ")()("
print(solution(s)) # False

s = "(()("
print(solution(s)) # False