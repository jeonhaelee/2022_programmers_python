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
    
    head1 = 0; tail1 = 0
    head2 = 0; tail2 = 0
    head3 = 0; tail3 = 0
    
    for i in range(len(s)):
        if s[i] == "[":
            head1 += 1
        elif s[i] == "]":
            tail1 += 1
        elif s[i] == "(":
            head2 += 1
        elif s[i] == ")":
            tail2 += 1
        elif s[i] == "{":
            head3 += 1
        elif s[i] == "}":
            tail3 += 1
        
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
    
    # 처음 입력받은 s가 올바른 괄호이면 값 리턴.
    result = check_true(s)
    if result:
        return result
    
    # s 회전하여 올바른 괄호인지 확인하기.
    count = 0
    while count < len(s):
        s = s[1:] + s[0]
        if check_true(s):
            return count
        else:
            count += 1
        
    return answer

s = "[](){}"
print(solution(s)) # 3

# s = "}]()[{"
# print(solution(s)) # 2

# s = "[)(]"
# print(solution(s)) # 0

# s = "}}}"
# print(solution(s)) # 0