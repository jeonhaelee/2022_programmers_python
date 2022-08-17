# 올바른 괄호

# 내 풀이
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

# 다른 사람 풀이 1
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

# 다른 사람 풀이 2
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0