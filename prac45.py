import math

def solution(n, words):
    answer = []
    finish = []
    
    for i in range(len(words)):
        if i == 0:
            finish.append(words[i])
            continue
        
        if words[i][0] != words[i-1][-1]:
            if (i+1)%n == 0:
                answer.append(n)
            else: answer.append((i+1)%n)
            answer.append(math.ceil((i+1)/n))
            return answer
        
        if words[i] in finish:
            if (i+1)%n == 0:
                answer.append(n)
            else: answer.append((i+1)%n)
            answer.append(math.ceil((i+1)/n))
            return answer

        finish.append(words[i])

    return [0,0]
