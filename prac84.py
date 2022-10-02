# 큰수만들기2

def solution(number, k):
    answer = []
   
    for n in number:
        while answer and k and n > answer[-1]:
            answer.pop()
            k -= 1
        answer.append(n)
    
    if k :
        return number[:-k]
    else:
        return ''.join(answer)

number = "1924"
k = 2
print(solution(number, k)) # "94"

number = "1231234"
k = 3
print(solution(number, k)) # "3234"

number = "4177252841"
k = 4
print(solution(number, k)) # "775841"