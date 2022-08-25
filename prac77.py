# 게임 맵 최단거리
# 검은색 : 벽, 흰색 : 길
# (진영에 도착 못 할 시, -1 리턴)

def solution(maps):
    answer = 0
    
    for x in range(5):
        for y in range(5):
            print(maps[x][y], end="")
        print()
    
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps)) # 11

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps)) # -1