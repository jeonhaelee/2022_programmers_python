def solution(s):
    answer = [] # answer의 크기는 len(s)
    d = []
    sub = []
    for i in range(len(s)-1):
        if s[i].isdigit():
            sub += s[i]
        if s[i] == "}":
            d.append(sub)
            sub = []
            if s[i+1] == "}":
                break
    print(d)
    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] not in answer:
                answer.append(d[i][j])
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))