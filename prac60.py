# 거리두기 확인하기
# 다시 생각해보자!
# 어차피 왼쪽 위에서 오른쪽 아래로 내려가는거니까...
# 기준 p에서 오른쪽이랑 아래랑 오른쪽 아래 대각선만 봐도 되는거 아닌가?
# 오른쪽에 X가 있으면 2오른쪽은 생각 안 해도 되고, 아래쪽에 X가 있으면 2아래쪽은 생각 안 해도 되고,
# 오른쪽에 X, 아래쪽에 X가 있으면 오른쪽아래대각선은 생각 안 해도 되니까.
# 이것들 중 X가 없을 경우에만 한칸 더 가서 P인지 아닌지만 따져주면 될 듯!!!


def check_place(place):
    place_list = []

    for i in range(len(place)):
        place_list.append((list(place[i])))
    
    for i in range(4):
        for j in range(4):
            if place_list[i][j] == 'P':
                if place_list[i][j+1] == 'P' or place_list[i+1][j] == 'P':
                    return 0
                
                if j >= 2:
                    pass
                else:
                    if place_list[i][j+2] == 'P':
                        if place_list[i][j+1] != 'X':
                            return 0
                        
                if i >= 2:
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
            if i > 3:
                pass
            else:
                if place_list[i+1][4] != 'X' and place_list[i+2][4] == 'P':    
                    return 0
                
    for i in range(4):
        if place_list[4][i] == 'P':
            if place_list[4][i+1] == 'P':
                return 0
            if i > 3:
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


