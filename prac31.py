def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            if s[i].islower():
                answer += s[i].upper()
            else: 
                answer += s[i]
        else:
            answer += s[i]
    return answer

# def solution(s):
#     answer = ''
#     words = s.split(" ")
#     for word in words:
#         for i in range(len(word)):
#             if i == 0:
#                 if word[0].islower():
#                     answer += word[0].upper()
#                 else: 
#                     answer += word[0]
#             else:
#                 answer += word[i]
#         answer += " "
#     return answer

s = "3people unFollowed me"
print(solution(s))