# 네트워크


def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(pc):
        visited[pc] = 1
        for idx, c in enumerate(computers[pc]):
            if c and visited[idx] != 1:
                dfs(idx)
        
    for pc in range(n):
        if visited[pc] == 0:
            dfs(pc)
            answer += 1
        
    return answer