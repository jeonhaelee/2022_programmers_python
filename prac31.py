def solution(s):
    answer = ''
    words = s.split(" ")
    for word in words:
        for i in range(len(word)):
            if i == 0:
                if word[0].islower():
                    answer += word[0].upper()
                else: 
                    answer += word[0]
            else:
                answer += word[i]
        answer += " "
    return answer

s = "3people unFollowed me"
print(solution(s))