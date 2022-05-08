

def solution(s):
    answer = [] # answer의 크기는 len(s)
    d = []
    sub = []
    for i in range(len(s)-1):
        if s[i].isdigit():
            sub += s[i]
        if s[i] == "}":
            d.append((sub, len(sub)))
            sub = []
            if s[i+1] == "}":
                break
    d.sort(key=lambda x:x[1])
    print(d)
    s2 = d[-1][0]
    print(s2)
    for num in s2:
        answer.append(num)
    print(answer)
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))