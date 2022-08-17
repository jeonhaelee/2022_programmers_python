# 삼각 달팽이


def solution(n):
    answer = []
    num = 1
    
    li = [[0] * n for i in range(n)]
    x = -1; y = 0
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            li[x][y] = num
            num += 1
    
    for i in range(n):
        print(li[i])
    
    return answer

n = 4
print(solution(n)) # [1,2,9,3,10,8,4,5,6,7]

n = 5
print(solution(n)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]