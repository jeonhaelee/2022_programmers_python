# 가장 먼 노드
from collections import deque

def solution(n, edge):
    answer = 0
    
    edge.sort() 
    
    l = [0] * (n+1) # 각 노드까지의 길이를 저장할 변수
    l[1] = 1 # 첫번째 노드는 1로 해준다. 왜? 나중에 edge가 [5, 1] 이런 식으로 나올 것을 대비해
    
    q = deque()
    graph = [[] for _ in range(n+1)] # 서로 연결되어 있는지 관계를 저장할 변수
    
    for e in edge: # 양방향이기 때문에 둘 다 append 해준다.
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    q.append(1) 
    while q:
        item = q.popleft()
        for g in graph[item]: # 해당 item과 연결된 노드 돌면서
            if l[g] == 0: # 해당 거리가 0이면
                q.append(g) # q에 g 노드 넣고
                l[g] = l[item] + 1 # g 노드까지의 거리를 l에 저장
        
        
    max_l = max(l) # l에서의 최대 길이를 찾아준다.
    for count in l:
        if count == max_l: # l을 돌며 그 값이 최대 길이이면 answer에 +1
            answer += 1
            
    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))