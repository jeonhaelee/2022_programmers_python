# 합승 택시 요금
# n : 지점 개수, s : 출발 지점, a : a 도착지, b : b 도착지

def solution(n, s, a, b, fares):
    answer = 0
    roads = [[1e9]*n for _ in range(n)]
    for i in range(n):
        roads[i][i] = 0

    
    for c, d, f in fares:
        roads[c-1][d-1] = f
        roads[d-1][c-1] = f
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if roads[i][j] > roads[i][k] + roads[k][j]:
                    roads[i][j] = roads[i][k] + roads[k][j]
    
    answer = 1e9
    for k in range(n):
        answer = min(answer, roads[s-1][k-1] + roads[k-1][a-1] + roads[k-1][b-1])
        
    return answer


n = 6; s = 4; a = 6; b = 2
fares = [[4, 1, 10], [3, 5, 24],
         [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
