def solution(s):
    answer = ''
    words = s.split(" ")
    for word in range(words):
        for i in range(len(word)):
            if word.isdigit() :
                answer += i
            elif word.
    return answer

s = "3people unFollowed me"
print(solution(s))