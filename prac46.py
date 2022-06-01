
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
    
    if p == "":
        return ""
    
    u = ""
    for i in range(len(p)):
        u += p[i]
        if u.count("(") == u. count(")"):
            if check(u):
                answer += u
                v = p[i+1:]
                answer += solution(v)
                break
            else:
                answer += "("
                v = p[i+1:]
                answer += solution(v)
                answer += ")"
                answer += change(u[1:len(u)-1])
                break

    return answer

p = "(()())()"
print('1번', solution(p)) #"(()())()"

p = ")("
print('2번', solution(p)) #"()"

p = "()))((()"
print('3번', solution(p)) #"()(())()"