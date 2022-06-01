
def check(u):
    left = 0; right = 0
    for i in range(len(u)):
        if u[i] == "(":
            left += 1
        elif u[i] == ")":
            right += 1
        if left < right:
            return False
    return True

def change(u):
    result = ""
    for i in range(len(u)):
        if u[i] == "(":
            result += ")"
        else: result += "("
    return result
    
    
    
def solution(p):
    answer = ""
    rear_answer = ""
    
    if p == "":
        return ""
    
    w = ""
    u = ""; v = ""
    for i in range(len(p)):
        if w.count("(") == w. count(")"):
            if check(u):
                answer += u
                v = p[i:]
                answer += solution(v)
            else:
                answer += "("
                v = p[i:]
                answer += solution(v)
                answer += ")"
                answer += change(u[1:len(u)])
        else: u += p[i]

    return answer

p = "(()())()"
print('1번', solution(p)) #"(()())()"

p = ")("
print('2번', solution(p)) #"()"