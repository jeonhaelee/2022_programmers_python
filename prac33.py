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
    for num in d[-1]:
        answer.append(num)
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))