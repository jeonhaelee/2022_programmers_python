def solution(n, words):
    answer = []
    finish = []
    
    for i in range(len(words)):
        if words[i] in finish:
            if (i+1)%3 == 0:
                answer.append(3)
            elif (i+1)%3 == 1:
                answer.append(1)
            elif (i+1)%3 == 2:
                answer.append(2)
            answer.append((i+1)//3)
        else:
            finish.append(words[i])

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))