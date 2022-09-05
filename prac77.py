# 게임 맵 최단거리
# 검은색 : 벽(0), 흰색 : 길(1)
# (진영에 도착 못 할 시, -1 리턴)

def draw_map(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            print(maps[i][j], end = "")
        print()

def solution(maps):

    n = len(maps); m = len(maps[0])

    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0:
        return -1
    
    
    x = 0; y = 0
    while x < n and y < m:
        print(f'x : {x}, y : {y}')
        draw_map(maps)
        
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




# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# print(solution(maps)) # 11

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps)) # -1