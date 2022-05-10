

# def solution(s):
#     answer = [] # answer의 크기는 len(s)
#     d = []
#     sub = []
#     num = ""
#     for i in range(len(s)-1):
#         if s[i].isdigit():
#             num += s[i]
#             if s[i+1] == "," or s[i+1] == "}":
#                 sub.append(int(num))
#                 num = ""
#         elif s[i] == "}":
#             d.append((sub, len(sub)))
#             sub = []
#             if s[i+1] == "}":
#                 break
#     d.sort(key=lambda x:x[1])
#     s2 = d[-1][0]
#     for num in s2:
#         answer.append(num)
#     return answer



def solution(s):
    answer = [] # answer의 크기는 len(s)
    d = []
    sub = []
    num = ""
    for i in range(1, len(s)-1):
        if s[i] == "{":
            sub = []
        if s[i].isdigit():
            num += s[i]
        if s[i] == ",":
            sub.append(int(num))
            num = ""
        if s[i] == "}":
            sub.append(int(num))
            d.append((sub, len(sub)))
            if s[i+1] == "}":
                break
    d.sort(key=lambda x:x[1])
    print(d)
    s2 = d[-1][0]
    print(s2)
    for num in s2:
        answer.append(num)
    return answer

s = "{{20,111},{111}}"
print(solution(s))