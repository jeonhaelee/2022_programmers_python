

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
            if s[i+1] == "{":
                continue
            sub.append(int(num))
            num = ""
        if s[i] == "}":
            sub.append(int(num))
            num = ""
            d.append(sub)
            if s[i+1] == "}":
                break
    d.sort(key=len)
    for nums in d:
        for num in nums:
            if num not in answer:
                answer.append(num)
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))