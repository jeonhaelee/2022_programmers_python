def solution(s):
    answer = [] # answer의 크기는 len(s)
    d = []
    sub = []
    num = ""
    for i in range(len(s)-1):
        if s[i].isdigit():
            num += s[i]
        if s[i] == ",":
            d.append(int(num))
        if s[i] == "}":
            d.append(sub)
            sub = []
            if s[i+1] == "}":
                break
    print(d)
    for num in d[-1]:
        answer.append(num)
    return answer

s = "{{20,111},{111}}"
print(solution(s))