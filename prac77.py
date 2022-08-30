# 게임 맵 최단거리
# 검은색 : 벽(0), 흰색 : 길(1)
# (진영에 도착 못 할 시, -1 리턴)

def solution(maps):

    n = len(maps); m = len(maps[0])
    
    for x in range(n):
        for y in range(m):
            print(maps[x][y], end="")
        print()
    
    # target_touch = False
    # count += 1
    # for x in range(5):
    #     for y in range(5):
    #         count += 1
    #         if maps[x][y] == 0:
    #             continue
    #         if x < 4:
    #             if maps[x+1][y] == 1:
    #                 break

    #         if x == 4 and y == 4:
    #             target_touch = True

    count = 0
    x = 0; y = 0
    while True:
        if maps[x+1][y] == 1:
            x += 1
            count += 1
        elif maps[x][y+1] == 1 :
            y += 1
            count += 1
        else:
            maps[x][y] = 0
            x -= 1
            count += 1
        
        if x == n and y == m:
            return count
        
        
        
        
        
        
    # if target_touch == True:
    #     return count
    # else:
    #     return -1
        


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps)) # 11

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps)) # -1