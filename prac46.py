def get_right(w):
    u = ""; v = ""
    for i in range(int(len(u)/2)):
        if u[i] != "(":
            answer += "("
            break
    answer += u


def solution(p):
    answer = ""
    rear_answer = ""
    
    if p == "":
        return ""
    
    w = ""
    for i in range(len(p)):
        if w.count("(") == w. count(")"):
            get_right(w)
            w = ""
        else: w += p[i]

    return answer

p = "(()())()"
print('1번', solution(p)) #"(()())()"

p = ")("
print('2번', solution(p)) #"()"