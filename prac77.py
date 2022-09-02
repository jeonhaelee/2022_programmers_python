# 게임 맵 최단거리
# 검은색 : 벽(0), 흰색 : 길(1)
# (진영에 도착 못 할 시, -1 리턴)

def solution(maps):

    n = len(maps); m = len(maps[0])

    count = 0
    x = 0; y = 0
    while count < 15:
        if x == n-1 and y == m-1:
            return count + 1
        
        if x+1 < n and y < m:
            if maps[x+1][y] == 1:
                maps[x][y] = 0
                x += 1
                count += 1
                continue
        if x < n and y+1 < m:
            if maps[x][y+1] == 1:
                maps[x][y] = 0
                y += 1
                count += 1
                continue
        if x-1 >= 0 and y < m:
            if maps[x-1][y] == 1:
                maps[x][y] = 0
                x -= 1
                count += 1
                continue
            else:
                break

    
    return -1




maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps)) # 11

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps)) # -1