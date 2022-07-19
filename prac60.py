# 거리두기 확인하기


# 내 풀이
def check_place(place):
    place_list = []

    for i in range(len(place)):
        place_list.append((list(place[i])))
    
    for i in range(4):
        for j in range(4):
            if place_list[i][j] == 'P':
                if place_list[i][j+1] == 'P' or place_list[i+1][j] == 'P':
                    return 0
                
                if j > 2:
                    pass
                else:
                    if place_list[i][j+2] == 'P':
                        if place_list[i][j+1] != 'X':
                            return 0
                        
                if i > 2:
                    pass
                else:
                    if place_list[i+2][j] == 'P':
                        if place_list[i+1][j] != 'X':
                            return 0
                        
                if place_list[i+1][j+1] == 'P':
                    if not (place_list[i][j+1] == 'X' and place_list[i+1][j] == 'X'):
                        return 0
                    
                if i >= 1:
                    if place_list[i-1][j+1] == 'P':
                        if not (place_list[i-1][j] == 'X' and place_list[i][j+1] == 'X'):
                            return 0
                    
    for i in range(4):
        if place_list[i][4] == 'P':
            if place_list[i+1][4] == 'P':
                return 0
            if i > 2:
                pass
            else:
                if place_list[i+1][4] != 'X' and place_list[i+2][4] == 'P':    
                    return 0
                
    for i in range(4):
        if place_list[4][i] == 'P':
            if place_list[4][i+1] == 'P':
                return 0
            if i > 2:
                pass
            else:
                if place_list[4][i+1] != 'X' and place_list[4][i+2] == 'P':    
                    return 0
            
            if place_list[3][i+1] == 'P':
                if not (place_list[3][i] == 'X' and place_list[4][i+1] == 'X'):
                    return 0
                        
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check_place(place))
        
    return answer

places = [["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places)) # [0, 0, 1, 1, 1]

# 다른 사람 풀이 1
def check(place):
    for irow, row in enumerate(place):
        for icol, cell in enumerate(row):
            if cell != 'P':
                continue
            if irow != 4 and place[irow + 1][icol] == 'P':
                return 0
            if icol != 4 and place[irow][icol + 1] == 'P':
                return 0
            if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X':
                return 0
            if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X':
                return 0
            if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
                return 0
            if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
                return 0
    return 1

def solution(places):
    return [check(place) for place in places]

# 다른 사람 풀이2
def solution(places):
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def f(i, j, cnt):
        nonlocal good
        if cnt >2 : return
        if -1<i<5 and -1<j<5:
            if graph[i][j] == 'X':
                return

            if cnt != 0 and graph[i][j] == 'P':
                good = 0
                return

            graph[i][j] = 'X'

            for w in range(4):
                ni = i+dx[w]
                nj = j+dy[w]
                f(ni, nj, cnt+1)

    for case in places:
        graph = [list(r) for r in case]
        good = 1
        for i in range(5):
            for j in range(5):
                if graph[i][j]=='P':
                    f(i,j,0)

        result.append(good)
    return result