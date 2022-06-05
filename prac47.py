# 2 x n 타일링
# 세로의 길이가 2, 가로의 길이가 n

def solution(n):
    
    count1 = 1; count2 = 2
    if n == 1:
        return count1
    elif n == 2:
        return count2
    for i in range(n-2):
        temp=count1
        count1=count2
        count2=count1+temp
    
    answer = count2%1000000007
    return answer

n = 4
print(solution(n))