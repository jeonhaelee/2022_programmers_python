def solution(n, words):
    answer = []
    finish = []
    
    for i in range(len(words)):
        if words[i] in finish:
            answer.append((i+1)%n)
            answer.append((i+1)//n)
        else:
            finish.append(words[i])

    return answer

n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", 
         "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))