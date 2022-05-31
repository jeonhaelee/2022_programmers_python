def solution(p):
    answer = ''
    if p == "":
        return ""
    
    u = ""
    v = ""
    for i in range(len(p)):
        if u.count("(") == u. count(")"):
            v += p[i]
        else: u += p[i]
        
    return answer

p = "(()())()"
print('1번', solution(p)) #"(()())()"

p = ")("
print('2번', solution(p)) #"()"