def solution(p):
    answer = ""
    rear_answer = ""
    
    if p == "":
        return ""
    
    u = ""
    v = ""
    for i in range(len(p)):
        if u.count("(") == u. count(")"):
            v += p[i]
        else: u += p[i]
    
    for i in range(len(u)/2):
        if u[i] != "(":
            
            break
    answer += u
    return answer

p = "(()())()"
print('1번', solution(p)) #"(()())()"

p = ")("
print('2번', solution(p)) #"()"