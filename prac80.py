# 괄호 회전하기


# 내 풀이
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
    
    head1 = 0; tail1 = 0
    head2 = 0; tail2 = 0
    head3 = 0; tail3 = 0
    
    for i in range(len(s)):
        if s[i] == "[":
            head1 += 1
        elif s[i] == "]":
            tail1 += 1
            if s[i-1] == "(" or s[i-1] == "{":
                return False
        elif s[i] == "(":
            head2 += 1
        elif s[i] == ")":
            tail2 += 1
            if s[i-1] == "[" or s[i-1] == "{":
                return False
        elif s[i] == "{":
            head3 += 1
        elif s[i] == "}":
            tail3 += 1
            if s[i-1] == "[" or s[i-1] == "(":
                return False
        
        if head1 < tail1:
            return False
        if head2 < tail2:
            return False
        if head3 < tail3:
            return False
        

        
    return True
    
    
def solution(s):
    answer = 0
    
    if len(s) % 2 != 0:
        return 0
    
    if not before_check(s):
        return 0
        
    # 처음 입력받은 s가 올바른 괄호인지 확인하기.
    print(f's : {s}')
    if check_true(s):
        answer += 1
    
    # s 회전하여 올바른 괄호인지 확인하기.
    count = 0
    while count < len(s) - 1:
        s = s[1:] + s[0]
        print(f's : {s}')
        
        if check_true(s):
            answer += 1
            count += 1
        else:
            count += 1
        
    return answer

s = "[](){}"
print(solution(s)) # 3

s = "}]()[{"
print(solution(s)) # 2

s = "[)(]"
print(solution(s)) # 0

s = "}}}"
print(solution(s)) # 0


# 다른 사람 풀이 1
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer


# 다른 사람 풀이 2
from collections import deque

def check(string):
    stack = []
    for s in string:
        if len(stack) == 0:
            if s == ')' or s == '}' or s == ']':
                return False
        if s == '(' or s == '{' or s == '[':
            stack.append(s)
        else:
            if s == ')' and stack[-1] == '(':
                stack.pop()
            elif s == '}' and stack[-1] == '{':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    queue = deque(list(s))
    i = 0
    while i != len(queue):
        if check(queue):
            answer += 1
        queue.rotate(-1)
        i += 1

    return answer