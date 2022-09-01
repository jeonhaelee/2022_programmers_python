# 게임 맵 최단거리
# 검은색 : 벽(0), 흰색 : 길(1)
# (진영에 도착 못 할 시, -1 리턴)

def solution(maps):

    n = len(maps); m = len(maps[0])
    
    for x in range(n):
        for y in range(m):
            print(maps[x][y], end="")
        print()

    count = 0
    x = 0; y = 0
    while x < n or y < m:
        if x + 1 < n:
            if maps[x+1][y] == 1:
                x += 1
                count += 1
        elif y + 1 < m:
            if maps[x][y+1] == 1:
                y += 1
                count += 1
        elif x - 1 >= 0:
            if maps[x-1][y] == 1:
                maps[x][y] = 0
                x -= 1
                count += 1
        
        if x == n-1 and y == m-1:
            return count
        
    return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps)) # 11

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# print(solution(maps)) # -1