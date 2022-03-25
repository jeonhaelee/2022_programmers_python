
def solution(n, m):
    answer = []
    answer1 = 0; answer2 = 0
    # 최대공약수를 넣어줄 answer1과 최소공배수를 넣어줄 answer2를 만들어줍니다.
    
    if m < n: # 보다 간단하게 하기 위해 n이 m보다 클 경우 둘의 자리를 바꿔줍니다.
        temp = n
        n = m
        m = temp
        
    for i in range(1,n+1): # 최대공약수 구하기
        if n % i == 0 and m % i == 0:
            answer1 = i
    
    for j in range(1,n*m+1): # 최소공배수 구하기
        if (j * m) % n == 0:
            answer2 = j * m
            break
    
    answer.append(answer1) # 구한 answer1과 answer2를 리스트 answer에 담아줍니다.
    answer.append(answer2)
    return answer # answer를 리턴해줍니다.
