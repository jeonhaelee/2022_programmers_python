
def solution(n, m):
    answer = []
    answer1 = 0; answer2 = 0
    
    if m < n:
        temp = n
        n = m
        m = temp
        
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            answer1 = i
    
    for j in range(1,n*m+1):
        if (j * m) % n == 0:
            answer2 = j * m
            break
    
    answer.append(answer1)
    answer.append(answer2)
    return answer
