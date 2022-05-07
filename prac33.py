def solution(s):
    answer = [] # answer의 크기는 len(s)
    d = []
    sub = []
    for i in range(len(s)):
        if s[i].isdigit():
            sub += s[i]
        if s[i] == "}":
            d.append(sub)
            sub = []
    print(d)
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))