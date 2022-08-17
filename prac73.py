# 삼각 달팽이

def solution(n):
    answer = []
    li = []

    for i in range(n):
        li.append([i+1])
        

    print(li)
    
    return answer

n = 4
print(solution(n)) # [1,2,9,3,10,8,4,5,6,7]

n = 5
print(solution(n)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]