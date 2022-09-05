# 게임 맵 최단거리
# 검은색 : 벽(0), 흰색 : 길(1)
# (진영에 도착 못 할 시, -1 리턴)

def solution(maps):

    n = len(maps); m = len(maps[0])

    x = 0; y = 0
    while x < n and y < m:
        print(f'x : {x}, y : {y}')
        
        if x == n-1 and y == m-1:
            return maps[n-1][m-1]
        
        if maps[x+1][y] == 1:
            maps[x+1][y] += maps[x][y]
            x += 1
            
        elif maps[x][y+1] == 1:
            maps[x][y+1] += maps[x][y]
            y += 1
            
        elif maps[x-1][y] == 1:
            maps[x-1][y] += maps[x][y]
            maps[x][y] = 0
            x -= 1
    
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1




maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps)) # 11

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# print(solution(maps)) # -1