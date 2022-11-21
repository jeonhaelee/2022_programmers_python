# 순위

def solution(n, results):
    answer = 0
    records = [[0]*n for _ in range(n)]
    
    for a, b in results:
        records[a-1][b-1] = 1
        records[b-1][a-1] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or records[i-1][j-1] == 1:
                    continue
                if records[i-1][k-1] == 1 and records[k-1][j-1] == 1:
                    records[i-1][j-1] = 1
                    records[j-1][i-1] = -1
                    records[k-1][i-1] = -1
                    records[j-1][k-1] = -1
    
    for r in records:
        print(r)
        if r.count(0) == 1:
            answer += 1
            
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))