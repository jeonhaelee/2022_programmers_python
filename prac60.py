# 거리두기 확인하기


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


