def solution(n, words):
    answer = []
    finish = []
    
    for i in range(len(words)):
        if words[i] in finish:
            answer.append((i+1)%3)
            answer.append((i+1)//3)


    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))