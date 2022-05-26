def solution(n, words):
    answer = []
    finish = []
    
    for i in range(len(words)):
        if words[i] in finish:
            answer.append((i+1)%n)
            answer.append((i+1)//n)
            return answer
        else:
            finish.append(words[i])

    return [0,0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))